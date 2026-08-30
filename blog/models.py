# blog/models.py
from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class BlogIndexPage(Page):
    parent_page_types = ["wagtailcore.Page"]
    subpage_types = ["blog.BlogPostPage"]
    max_count = 1

    intro = models.TextField(blank=True)
    featured_posts_count = models.IntegerField(default=3)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('featured_posts_count'),
    ]
    
    class Meta:
        verbose_name = "Blog Index"
    
    def get_posts(self, limit=None):
        posts = (
            BlogPostPage.objects.child_of(self)
            .live()
            .public()
            .order_by("-date", "-id")
        )
        if limit is not None:
            return posts[:max(limit, 0)]
        return posts
    
    def get_featured_posts(self):
        return self.get_posts(limit=self.featured_posts_count)


class BlogPostPage(Page):
    parent_page_types = ["blog.BlogIndexPage"]
    subpage_types = []

    date = models.DateField("Post date")
    intro = models.CharField(max_length=250, blank=True)
    body = models.TextField(blank=True)
    tags = models.CharField(max_length=255, blank=True)
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='featured_posts'
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('tags'),
        FieldPanel('featured_image'),
    ]
    
    class Meta:
        verbose_name = "Blog Post"
        ordering = ['-date', '-id']
    
    def get_tags_list(self):
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
        return []
