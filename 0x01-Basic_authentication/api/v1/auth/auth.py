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
    """
    Auth class signature
    """

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
        function that check request header and return its value
        :param request: take a request as a parameter
        :return: header value
        """
        if request is None or request.header.get("Authorization") is None:
            return None
        else:
            return request.header.get("Authorization")