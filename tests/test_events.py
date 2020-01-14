import unittest

from api.endpoints.events import EventsCollection, EventItem
from api.model import Event
from app import create_app


class FakeDBService(object):
    def get_all_events(self):
        return Event('_id', 'title', 'start_date', 'end_date', 'location', 'page')

    def get_event(self, id):
        return Event(id, 'title', 'start_date', 'end_date', 'location', 'page')


class TestEventsApi(unittest.TestCase):

    def setUp(self):
        EventsCollection.service = FakeDBService()
        EventItem.service = FakeDBService()
        self.app = create_app().test_client()

    def test_get_all_events(self):
        response = self.app.get('/api/events', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"title": "title"', response.data)

    def test_get_one_event(self):
        response = self.app.get('/api/events/100', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"title": "title"', response.data)
        self.assertIn(b'"id": "100"', response.data)


if __name__ == '__main__':
    unittest.main()
