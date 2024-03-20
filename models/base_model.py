#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """A class BaseModel that defines methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Initialize Public instance attributes"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, v in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        if isinstance(v, str):
                            datestyle = '%Y-%m-%dT%H:%M:%S.%f'
                            v = datetime.strptime(v, datestyle)
                    self.__dict__[key] = v
        else:
            storage.new(self)

    def __str__(self):
        """Return string"""
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """Save updated"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return to dictionary"""
        obj = self.__dict__.copy()
        obj['__class__'] = self.__class__.__name__
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj
