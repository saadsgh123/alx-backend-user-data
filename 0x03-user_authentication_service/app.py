#!/usr/bin/env python3
"""
main app
"""
from flask import Flask, request, jsonify, make_response, abort, render_template, redirect
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


@app.route("/sessions", methods=["POST"])
def login():
    """
    login and create a session id
    :return: respomse
    """
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not password:
        return abort(401)
    is_valid = AUTH.valid_login(email, password)
    if is_valid:
        session_id = AUTH.create_session(email)
        response = make_response(
            jsonify({"email": email, "message": "logged in"}))
        response.set_cookie("session_id", session_id)
        return response
    return abort(401)


@app.route("/sessions", methods=["DELETE"])
def logout():
    """
    logout function
    :return: response with 403 http if no user found
    """
    session_id = request.cookies.get("session_id")
    if session_id is not None:
        user = AUTH.get_user_from_session_id(session_id=session_id)
        AUTH.destroy_session(user.id)
        return redirect("/")
    else:
        response = make_response("", 403)
        return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
