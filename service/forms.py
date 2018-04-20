from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, AnyOf


class StoreForm(FlaskForm):
    class Meta:
        csrf = False
    message = StringField('message', validators=[DataRequired()])
    key = StringField('key', validators=[DataRequired()])
    submit = SubmitField('Store message')



class ReadForm(FlaskForm):
    class Meta:
        csrf = False
    mid = StringField('mid', validators=[DataRequired()])
    key = StringField('key', validators=[DataRequired()])
    submit = SubmitField('Store message')
