#!/usr/bin/python3
"""Doc
"""
from models.base_model import BaseModel
from datetime import datetime, date


class BaseModel(BaseModel):
    """Doc
    """

    def save(self):
        self.updated_at = datetime.utcnow()
