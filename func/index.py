import flask
from flask import Flask

blueprint = flask.Blueprint('profile', __name__, template_folder='templates')
