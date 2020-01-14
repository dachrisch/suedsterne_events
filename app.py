import logging.config
import os

from flask import Flask, Blueprint

import settings
from api.endpoints.events import ns as deployments_namespace
from api.restplus import api

logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), './logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def create_app():
    flask_app = Flask(__name__)

    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')

    api.init_app(blueprint)
    api.add_namespace(deployments_namespace)
    flask_app.register_blueprint(blueprint)

    return flask_app


def main():
    app = create_app()

    @app.route('/')
    def index():
        return '<br>'.join(['<a href="%s">%s</a>' % (p, p) for p in app.url_map.iter_rules()])

    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG, host=settings.FLASK_SERVER_HOST, port=settings.FLASK_SERVER_PORT)


if __name__ == "__main__":
    main()
