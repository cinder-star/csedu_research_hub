import pyrebase

from .config import config

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()