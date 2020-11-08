from os import path
from flask import Blueprint
from app.controllers.home import home


homeController = Blueprint('homeController', __name__, template_folder=path.abspath('app/views'))

    
homeController.add_url_rule('/',view_func=home)