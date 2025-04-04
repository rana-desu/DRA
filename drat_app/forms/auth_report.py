from flask_wtf import FlaskForm
from wtforms import (
    SubmitField,
    StringField,
    SelectField,
    IntegerField,
    BooleanField,
    TelField,
)
from wtforms.validators import (
    InputRequired,
    Length,
    NumberRange,
)

class AuthReportForm(FlaskForm):
    pass