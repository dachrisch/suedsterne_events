import mysql.connector

import settings
from api.model import Event


class EventsDBService(object):
    BASE_URL = 'https://it-agile.de'

    def get_all_events(self):
        cnx, cursor = self._get_cursor()
        cursor.execute("""SELECT training_date.uid, training.title, training_date.date_time, training_date.date_time_end, 
                                training_date.location, training.page
FROM `tx_events_domain_model_date` training_date
INNER JOIN `tx_events_event_date_mm` relationship ON training_date.uid = relationship.uid_foreign
INNER JOIN `tx_events_domain_model_event` training ON training.uid = relationship.uid_local
WHERE training_date.`location`='München' AND training_date.`date_time`>=CURDATE() """)

        events = []
        for row in cursor:
            _id, title, start_date, end_date, location, page = row
            events.append(Event(_id, title, start_date, end_date, location, self._resolve_link(page)))

        self._close(cnx, cursor)
        return events

    def get_event(self, _id):
        cnx, cursor = self._get_cursor(True)
        try:
            cursor.execute("""SELECT training.title, training_date.date_time, training_date.date_time_end, 
                                            training_date.location, training.page
            FROM `tx_events_domain_model_date` training_date
            INNER JOIN `tx_events_event_date_mm` relationship ON training_date.uid = relationship.uid_foreign
            INNER JOIN `tx_events_domain_model_event` training ON training.uid = relationship.uid_local
            WHERE training_date.uid = %s """, (_id,))

            title, start_date, end_date, location, page = cursor.fetchone()
        finally:
            self._close(cnx, cursor)

        return Event(_id, title, start_date, end_date, location, self._resolve_link(page))

    @staticmethod
    def _close(cnx, cursor):
        cursor.close()
        cnx.close()

    @staticmethod
    def _get_cursor(prepare_query=False):
        cnx = mysql.connector.connect(host=settings.DB_HOST, user=settings.DB_USER, passwd=settings.DB_PASSWORD,
                                      database=settings.DB_DATABASE)
        cursor = cnx.cursor(prepared=prepare_query)
        return cnx, cursor

    def _resolve_link(self, t3_link):
        url_part, uid_part = t3_link.split('?')
        uid_name, uid = uid_part.split('=')
        cnx, cursor = self._get_cursor(True)

        try:
            cursor.execute("""SELECT slug FROM `pages` WHERE uid = %s """, (uid,))
            (slug, ) = cursor.fetchone()
        finally:
            self._close(cnx, cursor)

        return '%s%s' % (EventsDBService.BASE_URL, slug)
