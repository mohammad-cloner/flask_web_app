import os
import pathlib
import requests
from flask import Blueprint, render_template, flash, url_for, session, abort, redirect, request,Flask,jsonify
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from google.oauth2 import id_token
import google.auth.transport.requests
from google_auth_oauthlib.flow import Flow
import random
import string
from pip._vendor import cachecontrol
from flask_mail import Message, Mail
import ssl,smtplib
import logging
from flask_wtf import CSRFProtect


app = Flask("__name__")
csrf = CSRFProtect(app)
auth = Blueprint('auth', __name__)
app.secret_key = 'ijhuljhu hukhouhku'
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

GOOGLE_CLIENT_ID = "*******************************.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "************************"
TELEGRAM_BOT_TOKEN = '***********************-******'
TELEGRAM_CHAT_ID = '-1002121162552'


flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/callback",
)


def send_telegram_message(chat_id, text):
    token = '6919607121:AAGCox6XvYbZfkcvmQyXiiobJi6oPm-49xo'
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': -1002121162552,
        'text': text,
        'parse_mode': 'HTML'
    }
    response = requests.post(url, data=payload)
    return response.ok


def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()

    return wrapper


def send_email(email, password):
    # Set up a basic logger
    logging.basicConfig(level=logging.INFO)

    msg = Message('Your Temporary Password', recipients=[email])
    msg.body = (f'Your temporary password is: {password}\n'
                'Please change your password after logging in. '
                'You can change your password here')

    try:
        mail = Mail(app)
        mail.send(msg)
        logging.info(f"Email sent to {email}")
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email to {email}: {e}")


@auth.route('/login', methods=['GET', 'POST'])
def login():


    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login2.html", user=current_user)


@auth.route('/login-bygoogle')
def login_bygoogle():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)


@auth.route('/callback')
def callback():


    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # Error: state does not match
    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)
    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )
    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    session["email"] = id_info.get("email")
    user = User.query.filter_by(email=session["email"]).first()
    if not user:
        plain_password = ''.join(random.choice(string.ascii_letters) for i in range(10))
        hashed_password = generate_password_hash(plain_password, method='pbkdf2:sha256')
        new_user = User(
            email=session["email"],
            first_name=session["name"],
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        user = new_user
        send_email(session["email"], plain_password)
    flash('Logged in successfully!', category='success')
    login_user(user, remember=True)
    return redirect(url_for('views.home'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email,first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)


@auth.route('/Task-note',methods=['GET', 'POST'])
def Task_note():

    return redirect(url_for('views.task'))




@auth.route('/send-to-telegram', methods=['POST'])
def send_to_telegram():
    data = request.get_json()
    message = data.get('message')

    is_sent = send_telegram_message('-1002121162552', message)
    return jsonify({'success': is_sent})

@auth.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')

        # Check if the new password and confirm password match
        if new_password != confirm_password:
            flash('Passwords do not match.', category='error')
            return redirect(url_for('auth.change_password'))

        # Update the password
        current_user.password = generate_password_hash(new_password, method='pbkdf2:sha256')
        db.session.commit()

        flash('Password updated successfully!', category='success')
        return redirect(url_for('views.setting'))

    return render_template("change_password.html", user=current_user)
