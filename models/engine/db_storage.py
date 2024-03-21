#!/usr/bin/python3
"""modules handles Database Storage """

import os
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base


class DBStorage:
    """handle storage of database"""
    __engine = None
    __session = None

    def __init__(self):
        """Public instance methods"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
            os.getenv("HBNB_MYSQL_USER"),
            os.getenv("HBNB_MYSQL_PWD"),
            os.getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """query all database"""
        session = self.__session()
        if cls:
            objects = session.query(cls).all()
        else:
            objects = session.query(Base).all()
            obj_dic = {}
            for obj in objects:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                obj_dic[key] = obj
            session.close()
            return result

    def new(self, obj):
        """add new odject"""
        self.__session.add(obj)

    def save(self):
        """commit changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj if not none"""
        if obj not None:
            self.__session.delete(obj)

    def reload(self):
        """reload all"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()
