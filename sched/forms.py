from wtforms import Form, BooleanField, DateTimeField
from wtforms import TextAreaField, TextField, PasswordField
from wtforms.validators import Length, required


class AppointmentForm(Form):
    """
    Plantilla para el formulario de appointment
    """
    title = TextField('Title', [Length(max=255)])
    start = DateTimeField('Start', [required()])
    end = DateTimeField('End')
    allday = BooleanField('All Day')
    location = TextField('Location', [Length(max=255)])
    description = TextAreaField('Description')


class LoginForm(Form):
    """
    Plantilla para el formulario de Login
    """
    username = TextField('Email', [required()])
    password = PasswordField('Password', [required()])
