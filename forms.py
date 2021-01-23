from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, validators

class ColorForm(FlaskForm):
    # number_of_colors = IntegerField("# color")
    submit = SubmitField("Generate Color!")
