import json
from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config.from_file("../config.json", load=json.load)

    from .blueprints import home
    home.register(app)

    from .blueprints import reports
    reports.register(app)

    from flask_wtf.csrf import CSRFProtect
    csrf = CSRFProtect(app)

    return app