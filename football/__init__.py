import os
import logging
from flask import Flask
from flask_cors import CORS
from flask_bootstrap import Bootstrap
from .config import get_config

app = Flask(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

logging.basicConfig(level=logging.DEBUG)

app.config['SECRET_KEY'] = get_config("SECRET_KEY")
app.config['ADMIN_USERNAME'] = get_config("ADMIN_USERNAME")
app.config['ADMIN_PASSWORD'] = get_config("ADMIN_PASSWORD")

Bootstrap(app)

basedir = os.path.abspath(os.path.dirname(__file__))

from pydal import DAL, Field

db = DAL('sqlite://' + os.path.join(basedir+"/db", 'storage.db') )

from .models import *

app.logger.info('App inicializada')