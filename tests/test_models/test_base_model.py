#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        self.model = BaseModel()

    def tearDown(self):
        del self.model
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        self.assertIsInstance(self.model, BaseModel)

    def test_kwargs_int(self):
        """ """
        with self.assertRaises(TypeError):
            BaseModel(**{1: 2})

    def test_save(self):
        """ Testing save """
        self.model.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_todict(self):
        """ """
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            BaseModel(**n)

    def test_kwargs_one(self):
        """ """
        with self.assertRaises(TypeError):
            BaseModel(Name='test')

    def test_id(self):
        """ """
       self.assertIsInstance(self.model.id, str)

    def test_updated_at(self):
        """ """
        self.assertIsInstance(self.model.created_at, datetime.datetime)
        self.assertIsInstance(self.model.updated_at, datetime.datetime)
