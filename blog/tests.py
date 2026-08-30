from datetime import date, timedelta
from io import StringIO

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse
from wagtail.models import Page
from wagtail.test.utils import WagtailPageTests

from .models import BlogIndexPage, BlogPostPage


class BlogPageTests(WagtailPageTests):
    def setUp(self):
        self.root = Page.objects.get(id=2)
        self.index_page = BlogIndexPage(
            title="Blog",
            intro="Notes about software and data.",
            slug="blog",
            live=False,
        )
        self.root.add_child(instance=self.index_page)
        self.index_page.save_revision().publish()
        self.index_page.refresh_from_db()

    def create_post(self, *, title, slug, post_date, live=True, **kwargs):
        post = BlogPostPage(
            title=title,
            slug=slug,
            date=post_date,
            live=False,
            **kwargs,
        )
        self.index_page.add_child(instance=post)
        revision = post.save_revision()
        if live:
            revision.publish()
        post.refresh_from_db()
        return post

    def test_page_type_restrictions(self):
        self.assertAllowedParentPageTypes(BlogIndexPage, [Page])
        self.assertAllowedSubpageTypes(BlogIndexPage, [BlogPostPage])
        self.assertAllowedParentPageTypes(BlogPostPage, [BlogIndexPage])
        self.assertAllowedSubpageTypes(BlogPostPage, [])
        self.assertCanCreateAt(Page, BlogIndexPage)
        self.assertCanCreateAt(BlogIndexPage, BlogPostPage)
        self.assertCanNotCreateAt(Page, BlogPostPage)
        self.assertCanNotCreateAt(BlogPostPage, BlogPostPage)

    def test_empty_index_renders_at_canonical_url(self):
        response = self.client.get("/blog/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts have been published yet.")

    def test_live_post_renders_at_public_url(self):
        post = self.create_post(
            title="First Post",
            slug="first-post",
            post_date=date.today(),
            intro="Intro text",
            body="Body text",
            tags="django, wagtail",
        )

        response = self.client.get("/blog/first-post/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)
        self.assertContains(response, "Body text")
        self.assertContains(response, "django")

    def test_posts_are_newest_first_and_featured_count_is_bounded(self):
        older = self.create_post(
            title="Older",
            slug="older",
            post_date=date.today() - timedelta(days=1),
        )
        newer = self.create_post(
            title="Newer",
            slug="newer",
            post_date=date.today(),
        )
        self.create_post(
            title="Unpublished Draft",
            slug="unpublished-draft",
            post_date=date.today() + timedelta(days=1),
            live=False,
        )
        self.index_page.featured_posts_count = 1

        self.assertEqual(list(self.index_page.get_posts()), [newer, older])
        self.assertEqual(list(self.index_page.get_featured_posts()), [newer])

        response = self.client.get("/blog/")
        content = response.content.decode()

        self.assertContains(response, "Newer")
        self.assertContains(response, "Older")
        self.assertNotContains(response, "Unpublished Draft")
        self.assertLess(content.index("Newer"), content.index("Older"))

    def test_draft_post_is_excluded_and_not_publicly_routable(self):
        draft = self.create_post(
            title="Draft",
            slug="draft",
            post_date=date.today(),
            live=False,
        )

        self.assertNotIn(draft, self.index_page.get_posts())
        self.assertEqual(self.client.get("/blog/draft/").status_code, 404)

    def test_tags_are_normalized_for_display(self):
        post = self.create_post(
            title="Tagged Post",
            slug="tagged-post",
            post_date=date.today(),
            tags="django, wagtail,  testing ",
        )

        self.assertEqual(post.get_tags_list(), ["django", "wagtail", "testing"])

    def test_post_image_is_optional(self):
        post = self.create_post(
            title="No Image Post",
            slug="no-image-post",
            post_date=date.today(),
        )

        self.assertIsNone(post.featured_image)


class BlogBootstrapCommandTests(TestCase):
    def test_command_creates_one_public_blog_index_and_is_idempotent(self):
        first_output = StringIO()
        second_output = StringIO()

        call_command("ensure_blog", stdout=first_output)
        call_command("ensure_blog", stdout=second_output)

        blog_indexes = BlogIndexPage.objects.filter(slug="blog")
        self.assertEqual(blog_indexes.count(), 1)
        self.assertTrue(blog_indexes.get().live)
        self.assertContains(self.client.get("/blog/"), "No posts have been published yet.")
        self.assertIn("Created the Wagtail blog index", first_output.getvalue())
        self.assertIn("already exists", second_output.getvalue())


class WagtailAdminTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username="wagtail-admin",
            email="admin@example.com",
            password="test-password",
        )
        root = Page.objects.get(id=2)
        self.index_page = BlogIndexPage(
            title="Blog",
            intro="Notes about software and data.",
            slug="blog",
        )
        root.add_child(instance=self.index_page)
        self.client.force_login(self.user)

    def test_admin_home_renders(self):
        response = self.client.get(reverse("wagtailadmin_home"))

        self.assertEqual(response.status_code, 200)

    def test_blog_index_editor_renders(self):
        response = self.client.get(
            reverse("wagtailadmin_pages:edit", args=(self.index_page.id,))
        )

        self.assertEqual(response.status_code, 200)
