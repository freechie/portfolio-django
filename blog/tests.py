from django.test import TestCase
from wagtail.models import Page
from wagtail.test.utils import WagtailPageTests
from .models import BlogIndexPage, BlogPostPage
from datetime import date

class BlogPageTests(WagtailPageTests):
    def setUp(self):
        # Ensure we have a root page to hang our content off
        self.root = Page.objects.get(id=2)

    def test_blog_index_page_creation(self):
        index_page = BlogIndexPage(
            title="My Blog",
            intro="Welcome to the blog",
            slug="blog"
        )
        self.root.add_child(instance=index_page)
        self.root.save()
        
        # Retrieve the page
        retrieved_page = BlogIndexPage.objects.get(title="My Blog")
        self.assertEqual(retrieved_page.intro, "Welcome to the blog")

    def test_blog_post_page_creation(self):
        # Create Index Page first
        index_page = BlogIndexPage(
            title="My Blog",
            slug="blog"
        )
        self.root.add_child(instance=index_page)
        
        # Create Blog Post
        blog_post = BlogPostPage(
            title="First Post",
            slug="first-post",
            intro="Intro text",
            body="Body text",
            date=date.today()
        )
        index_page.add_child(instance=blog_post)
        index_page.save()
        
        # Check if it exists
        self.assertTrue(BlogPostPage.objects.filter(title="First Post").exists())
        
        # Check parent relationship
        self.assertTrue(blog_post.get_parent().specific == index_page)

    def test_blog_post_tags_list(self):
        # Create Index Page
        index_page = BlogIndexPage(title="My Blog", slug="blog")
        self.root.add_child(instance=index_page)
        
        # Create Blog Post with tags
        blog_post = BlogPostPage(
            title="Tagged Post",
            slug="tagged-post",
            date=date.today(),
            tags="django, wagtail,  testing "  # Note extra spaces
        )
        index_page.add_child(instance=blog_post)
        index_page.save()
        
        # Verify get_tags_list splits and strips correctly
        tags_list = blog_post.get_tags_list()
        self.assertEqual(len(tags_list), 3)
        self.assertIn("django", tags_list)
        self.assertIn("wagtail", tags_list)
        self.assertIn("testing", tags_list)

    def test_blog_post_empty_tags(self):
        # Create Index Page
        index_page = BlogIndexPage(title="My Blog", slug="blog")
        self.root.add_child(instance=index_page)
        
        # Create Blog Post with NO tags
        blog_post = BlogPostPage(
            title="No Tag Post",
            slug="no-tag-post",
            date=date.today(),
            tags=""
        )
        index_page.add_child(instance=blog_post)
        index_page.save()
        
        # Verify empty list returned
        self.assertEqual(blog_post.get_tags_list(), [])

    def test_blog_post_optional_image(self):
         # Create Index Page
        index_page = BlogIndexPage(title="My Blog", slug="blog")
        self.root.add_child(instance=index_page)

        # Create Post without image
        blog_post = BlogPostPage(
            title="No Image Post",
            slug="no-image-post",
            date=date.today(),
            featured_image=None # explicitly None
        )
        index_page.add_child(instance=blog_post)
        index_page.save()
        
        self.assertIsNone(blog_post.featured_image)