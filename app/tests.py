"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase

# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_home(self):
        """Tests the home page."""
        response = self.client.get('/')
        self.assertContains(response, 'Home Page', 1, 200)

    def test_contact(self):
        """Tests the contact page."""
        response = self.client.get('/contact', follow=True)
        self.assertContains(response, 'Contact', 3, 200)

    def test_about(self):
        """Tests the about page."""
        response = self.client.get('/about', follow=True)
        self.assertContains(response, 'About', 3, 200)
        
    # def test_cv(self):
    #     """Tests the cv page."""
    #     response = self.client.get('/cv', follow=True)
    #     self.assertContains(response, 'CV', 4, 200)

    def test_cv2(self):
        """Tests the cv page."""
        response = self.client.get('/cv2', follow=True)
        self.assertContains(response, 'CV', 4, 200)

    def test_projects(self):
        """Tests the projects page."""
        response = self.client.get('/projects', follow=True)
        self.assertContains(response, 'Projects', 2, 200)

    def test_dontExist(self):
        """Tests a non-existing page."""
        response = self.client.get('/thispagedoesnotexist', follow=True)
        self.assertEqual(response.status_code, 404)