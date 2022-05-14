#!/usr/bin/python3
"""This module instantiates an object
of class DBStorage or FileStorage
"""
from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


type_storage = getenv('HBNB_TYPE_STORAGE')

if type_storage == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
