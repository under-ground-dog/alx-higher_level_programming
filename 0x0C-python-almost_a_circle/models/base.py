#!/usr/bin/python3
"""
base.py
"""
import json


class Base:
    """
    dostring
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        args: id - integer identity of base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        args: list_dictionaries -  is a list of dictionaries
        returns: the string: "[]" if list_dictionaries is None
        else the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        args: list_objs -  is a list of instances who inherits of Base

        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as My_file:
            if list_objs is None:
                My_file.write("[]")

            else:
                dict_list = []
                for obj in list_objs:
                    dict_list.append(obj.to_dictionary())
                My_file.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """
        args: json_string - is a string representing a list of dictionaries
        Returns: If json_string is None or empty, an empty list
        else the list represented by json_string
        """
        if json_string is None:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        args: **dictionary - can be thought of as double pointer to dictionary
        return: an instance with all attributes already set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            return new
