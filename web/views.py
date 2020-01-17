from bravado.client import SwaggerClient
from dateutil.parser import parse
from flask import url_for, render_template
from flask_classful import FlaskView

import settings


class EventsView(FlaskView):
    route_base = '/views'

    def index(self):
        client = SwaggerClient.from_url('http://%s:%s%s' % (
            settings.FLASK_SERVER_HOST, settings.FLASK_SERVER_PORT, url_for('api.specs')),
                                        config={'validate_responses': True})
        events = client.events.get_events_collection().response().result

        for event in events:
            event.start_date = parse(event.start_date).strftime('%d.%m.%Y')
            event.end_date = parse(event.end_date).strftime('%d.%m.%Y')

        return render_template('events.html', events=events)
