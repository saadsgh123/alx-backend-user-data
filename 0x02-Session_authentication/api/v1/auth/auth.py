#!/usr/bin/env python3
"""
Definition of class Auth
"""
import os
from typing import (
    List,
    TypeVar
)
from flask import request


class Auth:
    """
    Auth class signature
    """

    @staticmethod
    def require_auth(path: str, excluded_paths: List[str]) -> bool:
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
        function that check request header and return its value
        :param request: take a request as a parameter
        :return: header value
        """
        if request is None or request.headers.get("Authorization") is None:
            return None
        else:
            return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns a User instance from information from a request object
        """
        return None

    def session_cookie(self, request=None):
        """
        Returns a cookie from a request
        Args:
            request : request object
        Return:
            value of _my_session_id cookie from request object
        """
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_name)
