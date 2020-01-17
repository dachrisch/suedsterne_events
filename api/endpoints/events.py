import logging
from flask_restplus import Resource

from api.db.service import EventsDBService
from api.restplus import api
from api.serializers import event

log = logging.getLogger(__name__)

ns = api.namespace('events', description='Operations for Events')


@ns.route('/')
class EventsCollection(Resource):
    service = EventsDBService()

    @api.marshal_with(event, as_list=True)
    def get(self):
        return EventsCollection.service.get_all_events()


@ns.route('/<int:id>')
class EventItem(Resource):
    service = EventsDBService()

    @api.marshal_with(event)
    def get(self, id):
        return EventItem.service.get_event(id)
