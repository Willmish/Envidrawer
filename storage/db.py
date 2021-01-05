from storage.istorage import IStorage
from imports import logInfo, SensorData
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from os import getenv
from typing import List

class DBStorage(IStorage):
    def __init__(self):
        self.client = InfluxDBClient.from_env_properties()
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)
        self.bucket_name = getenv("DB_BUCKET")

    def write_all(self, records: List[SensorData]) -> bool:
        #logInfo("Saving data to DB")
        formatted = self.format_data(records)
        self.write_api.write(bucket=self.bucket_name, record=formatted)


    def write_single(self, record: SensorData) -> bool:
        logInfo("Saving a single record data to DB")
        pass

    def format_data(self, data: List[SensorData]) -> List[Point]:
        points: List[Point] = []
        for d in data:
            points.append(Point(d.name).tag("sensor_group", d.grp).field("val", d.val).time(d.time))

        return points

