class Event:
    id = 1
    start_date = 'name'
    end_date = 'action'
    title = 'scrum basics'
    location = 'munich'
    booking_link = 'https://it-agile.de/book.html'

    def __init__(self, _id, title, start_date, end_date, location, booking_link):
        self.booking_link = booking_link
        self.id = _id
        self.location = location
        self.end_date = end_date
        self.start_date = start_date
        self.title = title
