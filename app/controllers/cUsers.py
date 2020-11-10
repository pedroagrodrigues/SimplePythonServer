from flask import render_template, request, redirect, url_for

#Models used in this file must be imported
from app.models.mUser import checkUser

def login():
    if request.method == 'POST' and checkUser(request.form["username"], request.form['password']):
        return redirect(url_for("homeController.user", usr=user)) 
    return render_template("login.html", usr="Here I am sendig a variable to a view")

def user(usr):
  return f"Hello there {user}"
