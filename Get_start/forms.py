from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import  DataRequired, Length, Email, EqualTo
class Registration_form(FlaskForm):
    username = StringField("UserName",
                           validators= [DataRequired(), Length(min= 3, max= 25)])

    email= StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password",
                                     validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField("Sign Up")

class Signin_form(FlaskForm):
    email= StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign In")
