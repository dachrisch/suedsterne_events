from flask_restplus import fields

from api.restplus import api

event = api.model('Event', {
    'id': fields.String(readOnly=True, description='The unique identifier'),
    'start_date': fields.String(required=True, description='Start date of Event'),
    'end_date': fields.String(required=True, description='End date of Event'),
    'title': fields.String(required=True, description='Name of the Event'),
    'location': fields.String(reqired=True, description='Where the Event is happening'),
    'booking_link': fields.String(reqired=False, description='Link to book Event'),
})
