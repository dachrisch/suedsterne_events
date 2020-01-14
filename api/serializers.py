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

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

list_of_events = api.inherit('List of db', pagination, {
    'db': fields.List(fields.Nested(event))
})
