from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
    fixtures = ['site-fixtures.json']

    def setUp(self):
        self.views = {
            'home.index': 200,
            'twitch.live_status': 200,
            'twitch.agdq_streamers': 200,
        }

    def test_views(self):
        for view, status in self.views.items():
            print('Testing view "{}" for code "{}"'.format(view, status))
            response = self.client.get(reverse(view))
            self.assertEqual(response.status_code, status)
