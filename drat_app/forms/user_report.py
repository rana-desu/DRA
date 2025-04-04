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

class UserReportForm(FlaskForm):
    location = StringField(
        "Location",
        validators=[
            InputRequired(),
        ]
    )

    injury = SelectField(
        "Injuries",
        choices=[
            ("", "Select injury type"),  # Empty value as default
            ("cuts", "Minute cuts"),
            ("tear", "Muscle tear"),
            ("fracture", "Bone fracture"),
            ("wounds", "Rotten wounds"),
            ("blood_loss", "Heavy blood loss"),
            ("immobile", "Unable to move")
        ]
    )

    water = IntegerField(
        "Water",
        validators=[
            NumberRange(min=0, message="Value cannot be negative!")
        ]
    )

    food = IntegerField(
        "Food",
        validators=[
            NumberRange(min=0, message="Value cannot be negative!")
        ]
    )

    age_group = SelectField(
        "Age Group",
        choices=[
            ("", "Select Age Group"),  # Empty default
            ("child", "Child"),
            ("adult", "Adult"),
            ("senior", "Senior")
        ]
    )

    pregnant = BooleanField("Pregnant")
    gender = SelectField(
        "Gender", 
        choices=[
            ("", "Gender (optional)"),  # Empty value as default
            ("male", "Male"), 
            ("female", "Female"), 
            ("other", "Other"),
            ("none", "Prefer not to say")
        ]
    )
    mobile = TelField("Mobile")

    submit = SubmitField("Submit")