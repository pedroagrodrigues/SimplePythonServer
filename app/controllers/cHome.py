from flask import render_template, send_from_directory

def home():
    return render_template("index.html")

def favico():
    print("favico called")
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')