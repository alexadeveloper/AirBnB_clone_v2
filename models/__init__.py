#!/usr/bin/python3
"""create DB or FileStorage instance for your application"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import environ

try:
    if environ['HBNB_TYPE_STORAGE'] == 'db':
        storage = DBStorage()
        storage.reload()
except:
    storage = FileStorage()
    storage.reload()
