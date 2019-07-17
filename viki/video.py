import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class Video(object):
    def __init__(self, file):
        if isinstance(file, Path) is False:
            raise ValueError(f"{type(file)} is not from Path.")
        self.id = file

    def __repr__(self):
        return self.id

    def __str__(self):
        return self.id.name
