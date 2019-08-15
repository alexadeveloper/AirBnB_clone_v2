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
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from os import environ


class DBStorage:
    """Db storage class for airbnb proyect
    """
    __engine = None
    __session = None
    cls_all = {
            State,
            City}

    def __init__(self):
        """ Initial connection to sql database
        """
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                            environ['HBNB_MYSQL_USER'],
                            environ['HBNB_MYSQL_PWD'],
                            environ['HBNB_MYSQL_HOST'],
                            environ['HBNB_MYSQL_DB']),
                    pool_pre_ping=True)
        try:
            if environ['HBNB_ENV'] is 'test':
                for tbl in reversed(metadata.sorted_tables):
                    self.__engine.execute(tbl.delete())
        except:
            pass

    def all(self, cls=None):
        """ Return only one cls or all in dict form
        """
        items = {}
        if cls:
            qry = self.__session.query(eval(cls)).all()
            for value in qry:
                items.update({"{}.{}".format(
                    cls.__name__, value.id): value})
        else:
            for item in self.cls_all:
                qry = self.__session.query(item).all()
                for value in qry:
                    items.update(
                        {"{}.{}".format(
                            type(value).__name__, value.id): value})
        return items


    def new(self, obj):
        """ add the object to the current database session
        """
        if obj:
            self.__session.add(obj)

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
