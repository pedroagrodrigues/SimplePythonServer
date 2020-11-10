from flask import Flask, url_for
from settings import config

#Global variables

server = Flask(__name__)

if config.development:
    server.config.from_object(config.DevelopmentConfig)
else:
    server.config.from_object(config.ProductionConfig)


from app.controllers import homeController
server.register_blueprint(homeController)
