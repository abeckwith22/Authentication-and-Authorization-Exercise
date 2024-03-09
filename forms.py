from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Length

"""Forms"""

class RegistrationForm(FlaskForm):
    """Form for registering user to db."""

    username = StringField("Username:", validators=[InputRequired(message="Please enter a username")])
    password = PasswordField("Password:", validators=[InputRequired(message="Please enter a password")])
    email = StringField("E-mail Address:", validators=[InputRequired(message="Please enter a valid e-mail address")])
    first_name = StringField("First Name:", validators=[InputRequired(message="Please enter your first name")])
    last_name = StringField("Last Name:", validators=[InputRequired(message="Please enter your last name")])


class LoginForm(FlaskForm):
    """Form for logging a user in."""

    username = StringField("Username:", validators=[InputRequired(message="Please enter a username")])
    password = PasswordField("Password:", validators=[InputRequired(message="Please enter a password")])

class CreateFeedbackForm(FlaskForm):
    """Form for creating feedback."""

    title = StringField("Title:", validators=[InputRequired(message="Please enter a title"), Length(min=-1, max=100)])
    content = TextAreaField(validators=[InputRequired(message="Please enter some content"), Length(min=-1, max=100)])

class EditFeedbackForm(FlaskForm):
    """Form for editing feedback."""

    title = StringField("Title:", validators=[InputRequired(message="Please enter a title"), Length(min=-1, max=100)])
    content = TextAreaField(validators=[InputRequired(message="Please enter some content"), Length(min=-1, max=100)])
