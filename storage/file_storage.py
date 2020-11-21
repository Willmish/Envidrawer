from istorage import IStorage

class FileStorage(IStorage):
    def __init__(self, file_name):
        self.file_name = file_name

    def save(self, data):
        print("Saving data to file")

