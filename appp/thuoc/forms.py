from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, EmailField
from wtforms.validators import DataRequired, Email


class SearchingMedicineForm(FlaskForm):
    keyword = StringField("Tìm kiếm", render_kw={"placeholder": "Từ khóa"})
    submit = SubmitField("Tra cứu")

