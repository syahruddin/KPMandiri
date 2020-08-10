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
