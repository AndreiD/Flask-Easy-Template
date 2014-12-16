# -*- coding: utf-8 -*-

from app import *
from wtforms.validators import DataRequired, Length
from wtforms import Form, StringField, TextAreaField


class TasksAddForm(Form):
    title = StringField('title', validators=[DataRequired(), Length(max=255, message='max 255 characters')])
    description = TextAreaField('description', validators=[Length(max=200, message='max 200 characters')])





