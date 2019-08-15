#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from os import getenv

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state")
    else:
        def cities(self):
            """ Getter fuction for FileStorage mode
            """
            objs = models.storage.all()
            tmp = []
            for key, value in objs.items():
                name = key.split('.')
                if name[0] == "City":
                    if value.state_id == str(self.id):
                        tmp.append(objs[key])
            return tmp

