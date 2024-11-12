#!/usr/bin/env python3
from typing import List

from flask import request


class Auth:

    @staticmethod
    def require_auth(path: str, excluded_paths: List[str]) -> bool:
        return False

    @staticmethod
    def authorization_header(request=None) -> str:
        return None

    @staticmethod
    def current_user(request=None) -> TypeVar('User'):
        return None
