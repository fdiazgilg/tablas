from flask import Flask

app = Flask(__name__)

from tablas import routes

