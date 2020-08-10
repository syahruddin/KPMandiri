from flask import Blueprint, render_template, url_for, session, redirect, flash,request
from flask import current_app as app


from webapp.func import checkArgs
from webapp.mail.mail import sendConfirm
from webapp.query.query import getUserByUsername,setVerify,getUserbyEmail,newUser,changeEmail,changePass



import flask_login
from passlib.hash import sha256_crypt as sembunyi   #buat pass dll
from itsdangerous import URLSafeTimedSerializer


auth_bp = Blueprint('auth_bp', __name__, template_folder='templates',static_folder='static')

#login
@auth_bp.route('/logindef') #ini cuman buat nguji, nanti ga pakai ini halaman loginnya
def logindef():
    if not checkArgs(['username','password']):
        return "error",422
    else:
        username = request.args['username']
        password = request.args['password']

        attempt = fungsilogin(username,password)

        if attempt.accepted:
            if attempt.verified:
                #username dan password benar dan terverifikasi
                session['username'] = username
                return redirect(url_for('home_bp.index'))
            else:
                #belum terverifikasi
                return "akun belum terverifikasi"
        else:
            return "username atau password salah"

@auth_bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home_bp.index'))

#registrasi
@auth_bp.route('/api/reg')
def register():
    if not checkArgs(['username','email','password']):
        return "error",422
    else:
        #check apakah username terpakai
        username = request.args['username']
        sameUsername = str(getUserByUsername(username))
        userused = False
        if sameUsername != '[]':
            userused = True

        #check apakah email terpakai
        email = request.args['email']
        sameEmail = str(getUserbyEmail(email))
        emailused = False
        if sameEmail != '[]':
            emailused = True

        #memasukan data registrasi ke database jika username dan email belum terpakai
        if userused:
            flash('Username sudah terpakai')
            return 'userused'
        elif emailused:
            flash('Email sudah terpakai')
            return 'emailused'
        else:
            password = request.args['password']
            password = sembunyi.hash(password)
            newUser(email,username,password)
            sendConfirm(email)
            return 'ok',200


#setting
@auth_bp.route('/setting')
def setting():
    if not checkArgs(['username','email','password']):
        return "error",422
    else:
        username = request.args['username']
        email = request.args['email']
        password = request.args['password']

        #cari username (asumsi username bener(bakal ambil dari session buat manggil route ini))
        akun = getUserByUsername(username)[0]

        #cek password
        if not sembunyi.verify(password,akun[3]):
            return "password salah"
        else:
            #ganti email(kalau beda)
            if email != akun[1]:
                changeEmail(username,email)
            #ganti password(kalau ada args 'passwordnew')
            if checkArgs(['passwordnew']):
                passwordnew = request.args['passwordnew']
                changePass(username,sembunyi.hash(passwordnew))
            return "terganti"

#konfirmasi
@auth_bp.route('/confirm/<token>')
def confirm_email(token):
    try:
        confirm_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        email = confirm_serializer.loads(token, salt='email-confirmation-salt', max_age=3600)
    except:
        return 'invalid or expired'

    userconfirmed = getUserByEmail(email)[0][4]

    if userconfirmed:
        flash('Account already confirmed. Please login.', 'info')
    else:
        setVerify(email)
        flash('Thank you for confirming your email address!')
    return redirect(url_for('home_bp.index'))


#fungsi buat login, balikin tipe bentukan namanya attempt isinya 2 variabel boolean accepeted (username dan password bener) sama verified (udah terverifikasi)
def fungsilogin(username, password):

    attempting = attempt()

    #cari username
    akun = getUserByUsername(username)
    if str(akun) == '[]':
        attempting.accepted = False
    else:
        #cek password
        realpass = akun[0][3]
        if not sembunyi.verify(password,realpass):
            attempting.accepted = False
        else:
            #cek verifikasi
            attempting.verified = akun[0][4]

    return attempting

class attempt():
    accepted = True
    verified = True
