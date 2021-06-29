#!/usr/bin/python3
from models.engine.file_storage import FileStorage
"""
models module documentation

storage is a singleton to FileStorage
and reload objects to file.json
"""

storage = FileStorage()
storage.reload()
