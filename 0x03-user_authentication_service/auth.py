#!/usr/bin/env python3
import uuid

import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> bytes:
    """
    method that takes in a password and hash it.
    :param password:
    :return: returns bytes.
    """
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt(rounds=12)
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password


def _generate_uuid() -> str:
    """generate uuid"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        function takes email and password to create new user
        & throw a ValueError if already exists
        :param email: new user email
        :param password: new user password
        :return: User object.
        """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {user.email} already exists")
        except NoResultFound:
            new_user = self._db.add_user(email, _hash_password(password))
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        try:
            user = self._db.find_user_by(email=email)
            password_bytes = password.encode('utf-8')
            return bcrypt.checkpw(password_bytes, user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        create a new session id for the user
        :param email:
        :return: session id as string
        """
        user = self._db.find_user_by(email=email)
        if user is not None:
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        else:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """
        search for user by session id
        :param session_id:
        :return: User
        """
        if session_id is not None:
            try:
                user = self._db.find_user_by(session_id=session_id)
            except NoResultFound:
                return None
            return user

    def destroy_session(self, user_id: int) -> None:
        """
        Function that removes session_id from the database
        :param user_id:
        :return:
        """
        user = self._db.find_user_by(id=user_id)
        self._db.update_user(user.id, session_id=None)
        return None
