from flask_wtf import FlaskForm
from wtforms import StringField ,SubmitField

from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    name = StringField("Book Name", validators=[DataRequired(message="Please add a book title")])
    author = StringField("Book Author", validators=[DataRequired(message="Please add the author")])
    rating = StringField("Rating", validators=[DataRequired(message="Please add the rating")])
    submit = SubmitField('Add Book')