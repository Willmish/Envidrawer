from storage.istorage import IStorage
from imports import logInfo
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

class DBStorage(IStorage):
    def __init__(self):
        self.client = InfluxDBClient.from_env_properties()
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def write_all(self, record) -> bool:
        logInfo("Saving data to DB")

    def write_single(self, record) -> bool:
        logInfo("Saving a single record data to DB")
        pass

