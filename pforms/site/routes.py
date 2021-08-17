from flask import Blueprint, render_template, redirect, url_for, request, jsonify
import requests

site = Blueprint('site', __name__)
host = "http://localhost:5000"

@site.route('/')
def index():
    return render_template("index.html")

@site.route('/users/<id>')
def show_profile(id):
    res = requests.get(host + url_for('api.get_user', id=id))

    if res.ok:
        name = res.json()['username']
        return render_template('profile.html', user=name)
    else:
        return render_template('profile.html')

@site.route('/login')
def login():
    return render_template('login.html')

@site.route('/login', methods=['POST'])
def login_post():
    id = request.form.get('user')
    return redirect(url_for('site.show_profile', id=id))

@site.route('/signup')
def signup():
    return render_template('signup.html')

@site.route('/signup', methods=['POST'])
def signup_post():
    name = request.form.get('user')
    mail = request.form.get('mail')
    user = {"username": name, "email": mail}

    res = requests.post(host + url_for('api.add_user'), json=user)

    if res.ok:
        id=res.json()['id']
        return redirect(url_for('site.show_profile', id=id))
    else:
        return (res.text, res.status_code, res.headers.items())
