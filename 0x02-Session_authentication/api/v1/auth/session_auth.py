#!/usr/bin/env python3
"""
Definition of class Auth
"""
import uuid

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    class definition
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        if user_id is None and isinstance(user_id, str):
            return None
        else:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
