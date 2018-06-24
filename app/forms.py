# -*- coding: UTF-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, TextField
from wtforms.validators import DataRequired, Length


class CommentForm(FlaskForm):
    """ Form vaildator for comment."""

    name = StringField(
        'Name',
        validators=[DataRequired(), Length(max=255)]
    )

    text = TextField(u'Comment', validators=[DataRequired()])
