from pathlib import Path

from django.test import SimpleTestCase


class FrontendTests(SimpleTestCase):
    def test_projects_route_renders_built_bundle(self):
        response = self.client.get("/projects/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div id="app"></div>', html=True)

    def test_legacy_frontend_route_redirects_to_projects(self):
        response = self.client.get("/frontend/")

        self.assertRedirects(
            response,
            "/projects/",
            status_code=301,
            fetch_redirect_response=False,
        )

    def test_project_api_request_is_same_origin(self):
        source_path = Path(__file__).parent / "src" / "components" / "Responsive.js"
        source = source_path.read_text()

        self.assertIn('fetch("/api/projects/")', source)
        self.assertNotIn("http://localhost", source)

    def test_project_page_defines_user_visible_request_states(self):
        source_path = Path(__file__).parent / "src" / "components" / "Responsive.js"
        source = source_path.read_text()

        self.assertIn('role="status"', source)
        self.assertIn('role="alert"', source)
        self.assertIn("No projects are available yet.", source)
