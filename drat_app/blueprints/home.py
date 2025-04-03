from flask import (
    Flask,
    Blueprint,
    url_for,
    request,
    render_template,
    make_response,
    redirect
)

from drat_app.forms.report import ReportForm
from drat_app.data import DatabaseHelper as db
import jsonify


bp = Blueprint("home", __name__)

def register(app: Flask):
    app.register_blueprint(bp)

@bp.route("/", methods=["GET", "POST"])
def submit_report():
    """
    Displays:
    1. User Form: Submission for relevant user data (loaction, injuries, etc.)
    2. News Feed: Shows live updates for the relevant disaster occuring.
    """

    form = ReportForm()

    if form.validate_on_submit():
        print(form)
        report_data = {
            'location': form.location.data,
            'injury': form.injury.data,
            'food_hours': form.food.data,
            'water_hours': form.water.data,
            'age_group': form.age_group.data,
            'pregnant': form.pregnant.data,
            'gender': form.gender.data,
            'mobile': form.mobile.data
        }

        print(report_data)
        
        # db.insert_user_report(report_data)
        
        # Redirect to success page (prevents duplicate submissions)
        return render_template("index.html", form=form)

    return render_template("index.html", form=form)
    