from flask_sqlalchemy import SQLAlchemy   #sql
from flask_migrate import Migrate
import psycopg2   #biar bisa pakai query

from flask import Blueprint, render_template, url_for, redirect
from flask import current_app as app
from webapp.func import checkArgs

query_bp = Blueprint('query_bp', __name__, template_folder='templates',static_folder='static')


#setting sql query
conn = psycopg2.connect(app.config['SQLALCHEMY_DATABASE_URI'])
cur = conn.cursor()


def getUserByUsername(username):
    cur.execute("SELECT * FROM pengguna WHERE username = %s;",[username])
    data = cur.fetchall()
    return data

def getUserbyEmail(email):
    cur.execute("SELECT * FROM pengguna WHERE email = %s;",[email])
    data = cur.fetchall()
    return data

def newUser(email,username,password):
    cur.execute("INSERT INTO pengguna(email,username,pass) VALUES (%s,%s,%s);",[email,username,password])
    conn.commit()

def changePass(username,password):
    cur.execute("UPDATE pengguna SET pass = %s WHERE username = %s;",[password,username])
    conn.commit()

def changeEmail(username,email):
    cur.execute("UPDATE pengguna SET email = %s WHERE username = %s;",[email,username])
    conn.commit()

def setVerify(email):
    cur.execute("UPDATE pengguna SET verstatus = true WHERE email = %s;",[email])
    conn.commit()

def getProfil(username):
    cur.execute("select pengguna.userid, userprofil.name, userprofil.birthdate,userprofil.status,userprofil.phone,userprofil.phonehome,userprofil.email,userprofil.location,userprofil.address,userprofil.postnumber from userprofil inner join pengguna on pengguna.userid = userprofil.userid where pengguna.username = %s;",[username])
    data = cur.fetchall()
    return data

def setProfilName(name,username ):
    cur.execute("update userprofil set name = %s from pengguna where pengguna.userid = userprofil.userid and pengguna.username = %s;",[name,username])
    conn.commit()

def setProfilBirth(birthdate, username ):
    cur.execute("update userprofil set  birthdate = %s  from pengguna where pengguna.userid = userprofil.userid and pengguna.username = %s;",[birthdate,username])
    conn.commit()

def setProfilStatus(status, username ):
    cur.execute("update userprofil set status = %s  from pengguna where pengguna.userid = userprofil.userid and pengguna.username = %s;",[status,username])
    conn.commit()

def setProfilPhone(phone, username ):
    cur.execute("update userprofil set phone = %s from pengguna where pengguna.userid = userprofil.userid and pengguna.username = %s;",[phone,username])
    conn.commit()

def setProfilPhonehome( phonehome, username ):
    cur.execute("update userprofil set phonehome = %s from pengguna where pengguna.userid = userprofil.userid and pengguna.username = %s;",[phonehome,username])
    conn.commit()

def setProfilEmail(email,  username ):
    cur.execute("update userprofil set  email = %s from pengguna where pengguna.userid = userprofil.userid and pengguna.username = %s;",[email,username])
    conn.commit()

def setProfilLocation(location, username ):
    cur.execute("update userprofil set location = %s from pengguna where pengguna.userid = userprofil.userid and pengguna.username = %s;",[location,username])
    conn.commit()

def setProfilAddress(address, username ):
    cur.execute("update userprofil set address = %s from pengguna where pengguna.userid = userprofil.userid and pengguna.username = %s;",[address,username])
    conn.commit()

def setProfilPostnumber(postnumber, username ):
    cur.execute("update userprofil set  postnumber = %s  from pengguna where pengguna.userid = userprofil.userid and pengguna.username = %s;",[postnumber,username])
    conn.commit()

def setProfil(name,birthdate,status,phone,phonehome,email,location,address,postnumber,username):
    setProfilName(name,username )
    setProfilBirth(birthdate, username )
    setProfilStatus(status, username )
    setProfilPhone(phone, username )
    setProfilPhonehome( phonehome, username )
    setProfilEmail(email,  username )
    setProfilLocation(location, username )
    setProfilAddress(address, username )
    setProfilPostnumber(postnumber, username )
