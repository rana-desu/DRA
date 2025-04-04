from flask import (
    Flask,
    Blueprint,
    url_for,
    request,
    render_template,
    make_response,
    redirect
)

from drat_app.data import DatabaseHelper as db


bp = Blueprint("home", __name__)

def register(app: Flask):
    app.register_blueprint(bp)

@bp.route("/", methods=["GET", "POST"])
def index():
    """
    Displays the following content:
        1. Option to view reporting forms as:
            1. Auth Entities
            2. User Entities
        2. News Feed: Live updates.
    """

    return render_template("index.html")
