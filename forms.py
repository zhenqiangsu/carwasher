from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, StringField

from wtforms import validators, ValidationError
from wtforms.fields.html5 import TelField

class LoginForm(FlaskForm):
    phone = StringField('Phone', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.DataRequired() ])

class SignupForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=6, max=25)])
    phone = StringField('Username', [validators.Length(min=7, max=15)])
    email = StringField('Email Address', [validators.Length(min=6, max=60)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

class ContactForm(FlaskForm):
   name = TextField("Name", [validators.Required("Please enter your name.")])
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
   Address = TextAreaField("Address")
   
   email = TextField("Email",[validators.Required("Please enter your email address."),
      validators.Email("Please enter your email address.")])
   
   Age = IntegerField("age")
   language = SelectField('Languages', choices = [('cpp', 'C++'), 
      ('py', 'Python')])
   submit = SubmitField("Send")

class WashRequest(FlaskForm):
   name = StringField("Name", [validators.Required("Please enter your name.")])
   phone = TelField('Phone')
   Address = TextAreaField("Address")
   
   email = TextField("Email",[validators.Required("Please enter your email address."),
      validators.Email("Please enter your email address.")])
   
   Age = IntegerField("age")
   language = SelectField('Languages', choices = [('cpp', 'C++'), 
      ('py', 'Python')])
   submit = SubmitField("Send")

