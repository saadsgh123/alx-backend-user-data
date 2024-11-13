#!/usr/bin/env python3
"""
Definition of class Auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class signature
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header for a Basic
        Authorization
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        token = authorization_header.split(" ")[-1]
        return token
