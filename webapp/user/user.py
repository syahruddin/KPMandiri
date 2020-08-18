from flask import Blueprint, render_template, url_for, session, redirect, flash,request
from flask import current_app as app
from webapp.query.query import getProfil,setProfil
from webapp.func import checkArgs

user_bp = Blueprint('user_bp', __name__, template_folder='templates',static_folder='static')


@user_bp.route('/profil' ,methods=['POST','GET'])
def profil():
    if 'username' in session:
        if request.method == 'POST':
            username = session['username']
            name = request.form['name']
            print(name)
            print(type(name))
            birthdate = request.form['birthdate']
            print(birthdate)
            print(type(birthdate))
            if request.form['status'] == 'True':
                status = True
            else:
                status = False
            print(status)
            print(type(status))
            phone = request.form['phone']
            print(phone)
            print(type(phone))
            phonehome = request.form['phonehome']
            print(phonehome)
            print(type(phonehome))
            email = request.form['email']
            print(email)
            print(type(email))
            location = request.form['location']
            print(location)
            print(type(location))
            address = request.form['address']
            print(address)
            print(type(address))
            postnumber = request.form['postnumber']
            print(postnumber)
            print(type(postnumber))

            setProfil(name,birthdate,status,phone,phonehome,email,location,address,postnumber,username)
        else:
            data = getProfil(session['username'])
            name = data[0][1]
            birthdate = data[0][2]
            status = data[0][3]
            phone = data[0][4]
            phonehome = data[0][5]
            email = data[0][6]
            location = data[0][7]
            address = data[0][8]
            postnumber = data[0][9]

        return render_template('setting.html',name=name,birthdate=birthdate,status=status,phone=phone,phonehome=phonehome,email=email,location=location,address=address,postnumber=postnumber)
    else:
        return redirect(url_for('home_bp.index'))
