from flask import Flask
from flask_caching import Cache

cache = Cache(config={"CACHE_TYPE": "simple"})


def create_app(config_filename="config.py"):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)

    cache.init_app(app)

    from .main.views import main

    app.register_blueprint(main)

    return app
