from flask import Flask, render_template, request
from models import KomentarForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '@#123456&*()'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = KomentarForm()
    if request.method == 'POST':
        if form.validate():
            nama = form.nama.data
            email = form.email.data
            url = form.url.data
            komentar = form.komentar.data
            return render_template('response.html', nama=nama, email=email,
                                   url=url, komentar=komentar)

        else:
            errors = form.errors.items()
            return render_template('form.html', form=form, errors=errors)
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
