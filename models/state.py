#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete", backref="state")

    def get_cities(self):
        """ Getter fuction for FileStorage mode
        """
        objs = models.storage.all()
        tmp = []
        for key, value in objs.items():
            name = key.split('.')
            if name[0] == "City":
                tmp.append(objs[key])
        return tmp
