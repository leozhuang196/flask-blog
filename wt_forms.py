# -*- coding: UTF-8 -*-
from flask_wtf import Form
from wtforms import StringField, TextField
from wtforms.validators import DataRequired, Length


class CommentForm(Form):
    """ Form vaildator for comment."""

    name = StringField(
        'Name',
        vaildators=[DataRequired(), Length(max=255)]
    )

    text = TextField(u'Comment', validators=[DataRequired()])