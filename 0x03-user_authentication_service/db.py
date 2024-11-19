#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db",
                                     echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Create a User object and save it to the database
        Args:
            email (str): user's email address
            hashed_password (str): password hashed by bcrypt's hashpw
        Return:
            Newly created User object
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Return a user who has an attribute matching the attributes passed
        as arguments
        Args:
            attributes (dict): a dictionary of attributes to match the user
        Return:
            matching user or raise error
        """
        properties = User.__mapper__.attrs.keys()
        for k in kwargs.keys():
            if k not in properties:
                raise InvalidRequestError()
            user = self._session.query(User).filter_by(**kwargs).one()
            if user is None:
                raise NoResultFound()
            else:
                return user

    def update_user(self, user, hashed_password):
        """
        Update a user's attributes
        Args:
        user_id (int): user's id
        kwargs (dict): dict of key, value pairs representing the
            attributes to update and the values to update
            them with
        Return:
            No return
        """
        user = self.find_user_by(id=user)
        if user is None:
            raise ValueError()
        user.hashed_password = hashed_password
        return None
