# -*- coding: UTF-8 -*-
from flask import Flask
from config import DevConfig
import wt_forms

app = Flask(__name__)
# Import the views module
views = __import__('views')

# Get the config from object of DevConfig
app.config.from_object(DevConfig)

if __name__ == '__main__':
    # Entry the application
    app.run()
