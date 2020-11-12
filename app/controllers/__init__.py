from os import path
from flask import Blueprint

# Controlers functions
from app.controllers.cHome import home, favico, addNumbers
from app.controllers.cUsers import login, user

homeController = Blueprint('homeController', __name__, template_folder=path.abspath('app/views'))

# Routing 
# Home page
homeController.add_url_rule('/',view_func=home)
homeController.add_url_rule('/favicon.ico', view_func=favico)
homeController.add_url_rule('/addnumbers', view_func=addNumbers,  methods=["POST","GET"])

#User related pages
homeController.add_url_rule('/login/', view_func=login, methods=["POST","GET"])
homeController.add_url_rule('/<usr>', view_func=user)
