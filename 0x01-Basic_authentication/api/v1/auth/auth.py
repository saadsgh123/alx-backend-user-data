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
       Manages the API authentication
    """
    @staticmethod
    def require_auth(path: str, excluded_paths: List[str]) -> bool:
        """
            Determines whether a given path requires authentication or not
            Args:
                - path(str): Url path to be checked
                - excluded_paths(List of str): List of paths that do not require
                    authentication
            Return:
                 True if path is not in excluded_paths, else False
        """
        return False

    @staticmethod
    def authorization_header(request=None) -> str:
        """
            Returns the authorization header from a request object
        """
        return None

    @staticmethod
    def current_user(request=None) -> TypeVar('User'):
        """
            Returns a User instance from information from a request object
        """
        return None
