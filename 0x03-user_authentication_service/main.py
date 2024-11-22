#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth
from db import DB

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()
db = DB()

auth.register_user(email, password)

token = auth.get_reset_password_token(email="email")

print(token)
