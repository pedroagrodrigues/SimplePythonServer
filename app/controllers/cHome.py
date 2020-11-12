from flask import render_template, send_from_directory, jsonify, request
import sys

from Scripts.sumExemple import Exemple

def home():
    return render_template("index.html")

def favico():
    print("favico called")
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

def addNumbers():
    print("Reach the sum of a and b")
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    try:
        return jsonify(result=Exemple(a,b))

    except Exception as e:
        return jsonify(result=str(e))