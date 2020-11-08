from flask import Flask
from settings import config

#Global variables

server = Flask(__name__)

# server.config["ENV"] = "development"

if config.development:
    server.config.from_object(config.DevelopmentConfig)
else:
    server.config.from_object(config.ProductionConfig)

print(f'ENV is set to: {server.config["ENV"]}')

from app.controllers import homeController
server.register_blueprint(homeController)
