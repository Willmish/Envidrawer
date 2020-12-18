# Storage interface for either a file or DB

class IStorage():
    def write_all(self, record) -> bool:
        pass
    def write_single(self, record) -> bool:
        pass
