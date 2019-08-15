#!/usr/bin/python3
"""This is the DBStorage class for AirBnB"""
from sqlalchemy import (create_engine)
from sqlalchemy import MetaData
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from os import getenv


class DBStorage:
    """Db storage class for airbnb proyect
    """
    __engine = None
    __session = None
    name_cls = {
                "BaseModel": BaseModel,
                "State": State,
                "City": City,
                "User": User}

    def __init__(self):
        """ Initial connection to sql database
        """
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, passwd, host, db),
            pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            for tbl in reversed(metadata.sorted_tables):
                self.__engine.execute(tbl.delete())

    def all(self, cls=None):
        """ Return only one cls or all in dict form
        """
        if cls:
            items = self.__session.query(eval(cls)).all()
        else:
            items = self.__session.query(State, City).all()
        return items

    def new(self, obj):
        """ add the object to the current database session
        """
        if obj:
            self.__session.add(obj)
            self.save()

    def save(self):
        """ Commit changes to actual database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete object obj from db
        """
        if obj:
            for o in self.__session.query(State)\
                    .filter(State.name.like('{}'.format(obj)))\
                    .all():
                self.__session.delete(o)

    def reload(self):
        """ Reload tables and create session
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session()
