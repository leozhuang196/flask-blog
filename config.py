# -*- coding: UTF-8 -*-

class Config(object):
    """ Base config class. """
    SECRET_KEY = '0de6e8b914cb9d5530d194178195dae2'


class ProConfig(Config):
    """ Production config class. """
    pass


class DevConfig(Config):
    """ Development config class. """
    # Open the DEBUG
    DEBUG = True
    #MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:11444@127.0.0.1:3306/flask-blog'