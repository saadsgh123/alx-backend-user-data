#!/usr/bin/env python3
import bcrypt


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
