from storage.istorage import IStorage
from imports import logInfo

class FileStorage(IStorage):
    def __init__(self, file_name):
        self.file_name = file_name
        # open the file and close it

    def write_all(self, record) -> bool:
        logInfo("Saving data to file")

    def write_single(self, record) -> bool:
        pass

