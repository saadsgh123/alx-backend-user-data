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
print(f"token:{token}")

user = db.find_user_by(reset_token=token)
print(f"User password:{user.email}||{user.hashed_password}")

auth.update_password(reset_token=token, password="saadsghouri")
print(f"User password:{user.email}||{user.hashed_password}")

