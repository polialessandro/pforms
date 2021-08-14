from flask import Blueprint, render_template, redirect, url_for, request
from pforms import db
from pforms.models import User

site = Blueprint('site', __name__)

@site.route('/')
def index():
    return render_template("index.html")

@site.route('/users/<name>')
def show_profile(name):
    isuser = User.query.filter_by(username=name).first()
    if isuser:
        return render_template('profile.html', user=name)
    else:
        return render_template('profile.html')

@site.route('/login')
def login():
    return render_template('login.html')

@site.route('/login', methods=['POST'])
def login_post():
    user = request.form.get('user')
    return redirect(url_for('site.show_profile', name=user))

@site.route('/signup')
def signup():
    return render_template('signup.html')

@site.route('/signup', methods=['POST'])
def signup_post():
    name = request.form.get('user')
    mail = request.form.get('mail')
    user = User(username=name, email=mail)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('site.show_profile', name=name))