from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired

from mypage.models import CategoryEnum


class QuestionForm(FlaskForm):
    category = SelectField('Категория', choices=CategoryEnum.choices(), coerce=CategoryEnum.coerce)
    question = StringField('Вопрос', validators=[DataRequired()])
    detailed_description = TextAreaField('Детальное описание')
