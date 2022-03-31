import logging

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_mapping(SECRET_KEY='dev')


    from AppServer import versionapi, hello, favicon
    logging.basicConfig(level=logging.DEBUG)
    # apply the blueprints to the app
    app.register_blueprint(versionapi.bp)
    app.register_blueprint(favicon.bp)
    app.register_blueprint(hello.bp)

    return app