from flask_mail import Mail,Message #email
from flask import Blueprint, render_template, url_for, redirect
from flask import current_app as app
from webapp.func import checkArgs
from itsdangerous import URLSafeTimedSerializer


mail_bp = Blueprint('mail_bp', __name__, template_folder='templates',static_folder='static')
mail = Mail(app)
#fungsi buat ngirim email konfirmasi
def sendConfirm(email):
    confirm_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

    confirm_url = url_for('auth_bp.confirm_email',token=confirm_serializer.dumps(email, salt='email-confirmation-salt'),_external=True)

    html = render_template('email_confirmation.html',confirm_url=confirm_url)

    sendemail('Confirm Your Email Address', [email], html)

#fungsi buat ngirim email
def sendemail(subjek,penerima,html):
    msg = Message(subjek, sender=app.config['MAIL_USERNAME'], recipients=penerima)
    msg.html = html
    mail.send(msg)
