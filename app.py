from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '1e4d96d57ff01ef8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///site.db'

db = SQLAlchemy(app)

posts = [
    {
        'author': 'Yam',
        'title': 'Blog post 1',
        'content': 'This is an example for text',
        'date_posted': 'November 5, 2019',
    },
    {
        'author': 'John',
        'title': 'Blog post 2',
        'content': 'Lorem ipsum dolor sit amet',
        'date_posted': 'December 6, 2019',
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account has been created for user - { form.username.data }!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Registration', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'a@b.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Failed', 'danger')
    return render_template('login.html', title='Login', form=form)


# instead of flask run, python app.py
if __name__ == '__main__':
    app.run(debug=True)
