#!/usr/bin/env python3
"""
Definition of class Auth
"""
from typing import (
    List,
    TypeVar
)
from flask import request


class Auth:

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns the authorization header from a request object
        :param path:
        :param excluded_paths:
        :return:
        """
        if path is None:
            return True
        elif excluded_paths is None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        else:
            for i in excluded_paths:
                if i.startswith(path):
                    return False
                if path.startswith(i):
                    return False
                if i[-1] == "*":
                    if path.startswith(i[:-1]):
                        return False
        return True


    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header from a request object
        :return:
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns a User instance from information from a request object
        :param request:
        :return:
        """
        return None
