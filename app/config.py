# -*- coding: UTF-8 -*-

class Config(object):
    """Base config class."""
    # WTForm secret key
    SECRET_KEY = '0de6e8b914cb9d5530d194178195dae2'
    # reCAPTCHA Public key and Private key
    RECAPTCHA_PUBLIC_KEY = "6LfkjGAUAAAAAHn7-30iCMI6kFutFMPydOCtX1VA"
    RECAPTCHA_PRIVATE_KEY = "6LfkjGAUAAAAAF-byKLdA3yf6-ubmo6ZgeWX_4YI"

class ProConfig(Config):
    """ Production config class. """
    pass


class DevConfig(Config):
    """ Development config class. """
    # Open the DEBUG
    DEBUG = True
    #MySQL connection
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:#^hi3%X#@127.0.0.1:3306/flask-blog'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:11444@127.0.0.1:3306/flask-blog'
