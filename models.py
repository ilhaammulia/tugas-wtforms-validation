from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length, Email, URL


class KomentarForm(FlaskForm):
    nama = StringField('Nama:', validators=[
                       InputRequired('Nama harus diisi!'), Length(max=25)])
    email = StringField('Email:', validators=[InputRequired(
        'Email harus diisi!'), Email('Alamat email tidak ditulis dengan benar.')])
    url = StringField('URL:', validators=[
                      InputRequired('URL harus diisi!'), URL()])
    komentar = TextAreaField('Komentar:', validators=[
                             InputRequired('Komentar harus diisi!')])
    submit = SubmitField('Kirim')
