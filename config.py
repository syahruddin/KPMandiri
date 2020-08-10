from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir,'.env'))

UPLOAD_FOLDER =  basedir + environ.get('LOKA')

class Config:
    UPLOAD_FOLDER = UPLOAD_FOLDER      #setting upload

    SECRET_KEY = environ.get('SECRET_KEY')

        #pengaturan database
    SQLALCHEMY_DATABASE_URI =environ.get('SQLURL')
        #setting email
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = environ.get('MAIL_PASS')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True



    DEBUG = True   #jadiin false pas deployment
