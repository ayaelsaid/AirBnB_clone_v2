#!/usr/bin/python3
"""
the class TestConsole
"""

from console import HBNBCommand
import inspect
import pep8
import unittest


class Testconsole(unittest.TestCase):

    def test_empty_args(self):
        result = HBNBCommand().do_create("")
        self.assertEqual(result, "** class name missing **")

    def test_class_not_in_classes(self):
        result = HBNBCommand().do_create("Bat")
        self.assertEqual(result, "** class doesn't exist **")

    def test_do_dic(self):
        result = HBNBCommand().do_create('User name="California"\
                                         id=4 grad=5.5')
        self.assertIsInstance(result, str)

    def test_datatype_value(self):
        result_str = HBNBCommand().do_create('Place city_id="0001"\
                                             user_id="0001" name="My_little_house"\
                                             number_rooms=4 number_bathrooms=2 max_guest=10\
                                             price_by_night=300\
                                             latitude=37.773972 longitude=-122.431297')
        self.assertIsInstance(result_str, str)


if __name__ == "__main__":
    unittest.main()
