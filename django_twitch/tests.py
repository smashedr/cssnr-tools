from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
    fixtures = ['site-fixtures.json']

    def setUp(self):
        self.views = {
            'home_view': 200,
            'about_view': 200,
            'members_view': 302,
        }

    def test_views(self):
        for view, status in self.views.items():
            print('Testing view "{}" for code "{}"'.format(view, status))
            response = self.client.get(reverse(view))
            self.assertEqual(response.status_code, status)