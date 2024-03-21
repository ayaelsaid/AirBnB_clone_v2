#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    if os.gentev('HBNB_TYPE_STORAGE') = 'db':
        reviews = relationship('Review', cascade='all, delete',
                               backref='place')
    else:

        @property
        def reviews(self):
            """ method for reviews """
            from models import storage
            from models.review import Review
            new_list = []
            re_dict = storage.all(Review)
            for re in re_dict.values():
                if review.place_id == self.id:
                    new_list.append(city)
            return new_list
