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
from os import environ


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
        if cls:
            items = self.__session.query(eval(cls)).all()
        else:
            ''' Here is the problem need the correct format'''
            items = self.__session.query(State, City).all()
            '''
            new_dict = {}
            for i in range(len(items)):
                print(items[i])

                tmp = items[i].to_dict()
                print("*** tmp ***", tmp)
                new_dict[str(items[i].__class__.__name__) +
                        "." +
                        str(items[i].id)] = tmp
            new_dict2 = {}
            for key, value in (new_dict).items():
                print("*** value ***", value)
                value = eval(value["__class__"])(**value)
                print("*** key ***", key)
                new_dict2[key] = value
            '''
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
