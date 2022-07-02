from flask import Flask

import logger
from bp_api.views import blueprint_api
from bp_posts.views import bp_posts
from exceptions.data_exceptions import DataSourceError


def create_and_config_app(config_path):
    app = Flask(__name__)

    app.register_blueprint(bp_posts)
    app.register_blueprint(blueprint_api, url_prefix='/api')
    app.config["JSON_AS_ASCII"] = False
    app.config.from_pyfile(config_path)
    logger.config(app)
    return app


app = create_and_config_app("config.py")


@app.errorhandler(404)
def page_error_404(error):
    return f"Нет такой страницы {error}", 404


@app.errorhandler(500)
def page_error_500(error):
    return f"Something wrong on server - {error}", 500


@app.errorhandler(DataSourceError)
def page_error_data_source_error(error):
    return f"Data on server are broken - {error}", DataSourceError


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
