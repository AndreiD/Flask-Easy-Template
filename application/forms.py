from wtforms import Form, StringField, TextAreaField, validators


class Form_Record_Add(Form):
    title = StringField('title', validators=[validators.DataRequired(),
                                             validators.Length(max=255, message='max 255 characters')])
    description = TextAreaField('description',
                                validators=[validators.Length(max=200, message='max 200 characters')])
