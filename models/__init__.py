#!/usr/bin/python3
"""Module for instantiation of unique FileStorage instance."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
