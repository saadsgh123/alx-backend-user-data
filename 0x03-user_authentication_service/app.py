#!/usr/bin/env python3
"""
main app
"""
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
    :return: message
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}, 400)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
