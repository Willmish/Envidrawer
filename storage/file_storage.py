from storage.istorage import IStorage
from imports import logger

class FileStorage(IStorage):
    def __init__(self, file_name):
        self.file_name = file_name

    def save(self, data):
        logger.info("Saving data to file")

