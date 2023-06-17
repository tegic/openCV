from flask import Flask, render_template, url_for, request
from flask_wtf import FlaskForm, Form
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField
from werkzeug.utils import secure_filename
import os
import wb_functions

class MyForm(FlaskForm):
    file = FileField( 'Upload photo ↓' ,id='file_field', validators=[
        FileRequired(), 
        FileAllowed(
            ['jpg', 'png'], 'Images only!'
        )
    ])
    submit = SubmitField('Submit', id='submit_field')



app = Flask(__name__)

@app.route('/main_page', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def main_page():
    file_field = MyForm()
    if request.method == 'POST':
        f = file_field.file.data
        filename = f.filename
        # filename = secure_filename(f.filename)
        path = f'static\photos\{filename}'
        # os.path.join(
        #     app.instance_path, 'photos', filename
        # )
        f.save(path)
        new_filename = wb_functions.image_loader(filename, path)
        print(filename)
        return render_template('main_page.html', form=file_field, img=new_filename)
    return render_template('main_page.html', form=file_field)


@app.route('/about_us_page')
def about_us_page():
    return render_template('about_us_page.html')


@app.route('/other_products_page')
def other_products_page():
    return render_template('other_products_page.html')

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'test'
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = 'tssss it is a secret key'
    app.run(debug=True)
    form = FlaskForm(meta={'csrf': True})