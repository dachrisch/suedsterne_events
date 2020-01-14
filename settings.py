# Flask settings
import os

FLASK_SERVER_HOST = os.getenv('EVENTS_SERVICE_HOST', 'localhost')
FLASK_SERVER_PORT = os.getenv('EVENTS_SERVICE_PORT', '8888')
FLASK_SERVER_NAME = '%s:%s' % (FLASK_SERVER_HOST, FLASK_SERVER_PORT)
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# DB properties
DB_HOST = 'sql528.your-server.de'
DB_USER = os.getenv('DB_USER', 'user')
DB_PASSWORD = os.getenv('DB_PASSWD', 'password')
DB_DATABASE = 'itwagi_db1'
