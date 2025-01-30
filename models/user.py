#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import hashlib


class User(BaseModel, Base):
    """Representation of a user"""
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes user"""
        super().__init__(*args, **kwargs)
        if 'password' in kwargs:
            self.password = kwargs['password']  # Calls setter to hash password

    @staticmethod
    def hash_password(password):
        """Hashes password using MD5"""
        return hashlib.md5(password.encode()).hexdigest()

    @property
    def password(self):
        """Getter for password (returns hashed password)"""
        return getattr(self, "_password", None)  # Use getattr instead of __dict__

    @password.setter
    def password(self, value):
        """Setter for password, hashes it before storing"""
        hashed_value = User.hash_password(
            value)  # Explicitly call static method
        setattr(self, "_password", hashed_value)  # Store properly
