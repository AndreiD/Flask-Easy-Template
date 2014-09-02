# -*- coding: utf-8 -*-

from app import *
from wtforms.validators import Required, Length
from wtforms import Form, TextField, TextAreaField


class ExpensesInfoForm(Form):
    title = TextField('title', validators=[Required(), Length(max=255, message='max 255 characters')])
    description = TextAreaField('description', validators=[Length(max=200, message='max 200 characters')])
    color_code = TextField('color_code', default="#FFFFFF",  validators=[Required(), Length(max=7, message='max 7 characters')])




