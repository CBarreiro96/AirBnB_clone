#!/usr/bin/python3
"""
storage module
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
