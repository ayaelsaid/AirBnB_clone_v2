#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        mycities = relationship("City", cascade="all, delete-orphan",
                                backref="state")
    else:

        def mycities(self):
            """ method for cities """
            from models import storage
            from models.city import City
            new_list = []
            cities_dict = storage.all(City)
            for city in cities_dict.values():
                if city.state_id == self.id:
                    new_list.append(city)
            return new_list
