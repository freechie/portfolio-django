from django.core.management.base import BaseCommand, CommandError
from wagtail.models import Page, Site

from blog.models import BlogIndexPage


class Command(BaseCommand):
    help = "Create and publish the canonical Wagtail blog index if it is missing."

    def handle(self, *args, **options):
        site = (
            Site.objects.filter(is_default_site=True).select_related("root_page").first()
            or Site.objects.select_related("root_page").first()
        )
        if site is None:
            raise CommandError("No Wagtail site exists. Run migrations first.")

        root_page = site.root_page.specific
        existing_page = Page.objects.child_of(root_page).filter(slug="blog").first()

        if existing_page is not None:
            if not isinstance(existing_page.specific, BlogIndexPage):
                raise CommandError(
                    f'Cannot create the blog because "{existing_page.title}" already uses /blog/.'
                )
            self.stdout.write("The Wagtail blog index already exists.")
            return

        if BlogIndexPage.objects.exists():
            raise CommandError(
                "A blog index already exists outside the default site's root page."
            )

        blog_index = BlogIndexPage(
            title="Blog",
            slug="blog",
            intro="Notes about software, data, and the work behind this portfolio.",
            live=False,
        )
        root_page.add_child(instance=blog_index)
        blog_index.save_revision().publish()
        self.stdout.write(self.style.SUCCESS("Created the Wagtail blog index at /blog/."))
