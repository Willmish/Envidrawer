from storage.istorage import IStorage
from imports import logInfo

class FileStorage(IStorage):
    def __init__(self, file_name):
        self.file_name = file_name

    def save(self, data):
        logInfo("Saving data to file")

