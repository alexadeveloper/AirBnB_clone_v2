#!/usr/bin/python3
"""This is the place class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id',
                             String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        def get_amenities(self):
            """ Getter function for FileStorage mode
            """
            objs = models.storage.all()
            tmp = []
            for key, value in objs.items():
                name = key.split('.')
                if name[0] == "Amenity":
                    for item in self.amenity_ids:
                        if item == name[1]:
                            tmp.append(val)
            return tmp

        def set_amenities(self, obj):
            """ Setter function for FileStorage mode
            """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)

        def get_reviews(self):
            """ Getter fuction for FileStorage mode
            """
            objs = models.storage.all()
            tmp = []
            for key, value in objs.items():
                name = key.split('.')
                if name[0] == "Review":
                    if value.place_id == str(self.id):
                        tmp.append(val)
            return tmp
