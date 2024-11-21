#!/usr/bin/env python3
from flask import Flask, request, jsonify
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def welcome():
    """
    welcome to route
    :return: response json object
    """
    response = {"message": "Bienvenue"}
    return jsonify(response)


@app.route("/users", methods=["POST"])
def register():
    """
    create a new user
    :return:
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return {"email":email, "message":"user created"}
    except ValueError:
        return {"message": "email already registered"}





if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
