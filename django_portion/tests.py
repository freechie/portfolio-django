from django.test import TestCase, Client
from django.urls import reverse
from .models import Project, Skill, Resume

class ProjectModelTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="Test Project",
            description="A test description",
            repo_link="http://example.com"
        )

    def test_project_string_representation(self):
        self.assertEqual(str(self.project), "Test Project")

    def test_project_defaults(self):
        self.assertEqual(self.project.status, 'in_progress')
        self.assertFalse(self.project.is_featured)


class SkillModelTest(TestCase):
    def setUp(self):
        self.skill = Skill.objects.create(
            name="Python",
            proficiency=90
        )

    def test_skill_string_representation(self):
        self.assertEqual(str(self.skill), "Python")


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Create dummy resume for resume view
        Resume.objects.create(title="My Resume", upload="resume.pdf")

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'django_portion/index.html')

    def test_project_index_view(self):
        response = self.client.get(reverse('project_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'django_portion/project_index.html')

    def test_skills_index_view(self):
        response = self.client.get(reverse('skills_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'django_portion/skills_index.html')

    def test_about_me_view(self):
        response = self.client.get(reverse('about_me'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'django_portion/about_me.html')

    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'django_portion/contact.html')

    def test_resume_view(self):
        response = self.client.get(reverse('resume'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'django_portion/resume.html')

    def test_resume_view_empty(self):
        # Delete the setup resume to test empty state
        Resume.objects.all().delete()
        response = self.client.get(reverse('resume'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'django_portion/resume.html')
        self.assertIsNone(response.context['resume'])

    def test_project_detail_404(self):
        # Test accessing a non-existent project ID
        response = self.client.get(reverse('project_detail', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_blog_detail_404(self):
        # Test accessing a non-existent blog post ID
        response = self.client.get(reverse('blog_detail', args=[999]))
        self.assertEqual(response.status_code, 404)
        
    def test_blog_by_tag_empty(self):
        # Test accessing a tag that doesn't exist
        response = self.client.get(reverse('blog_by_tag', args=['nonexistent']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'django_portion/tagged_content.html')
        self.assertEqual(len(response.context['display_items']['posts']), 0)
        self.assertEqual(len(response.context['display_items']['projects']), 0)