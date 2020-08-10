from flask import Blueprint, render_template, url_for, redirect,session
from flask import current_app as app
from webapp.func import checkArgs

home_bp = Blueprint('home_bp', __name__, template_folder='templates',static_folder='static')


#halaman utama, tapi sementara dipakai testing
@home_bp.route('/')
def index():
    if 'username' in session:
        return 'hello, ' + str(session['username'])
    return 'belum login'
