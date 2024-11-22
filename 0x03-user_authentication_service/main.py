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

session_id = auth.create_session(email)

print(f"Session id:{session_id}")

search_user = db.find_user_by(email=email)
print(search_user.session_id)

user = auth.get_user_from_session_id("session_id")
print(user.email)
