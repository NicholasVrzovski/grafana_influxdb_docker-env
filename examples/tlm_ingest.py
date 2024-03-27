
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from random import uniform
import datetime as dt
import pytz
import time


INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = "478fQSqlIKsHX8c1vE43hS8uXPdvN1v4WVnS73MSUBpNeZ6TW0iTB-NNnOzAgwINY4k21uI8xVaD4_K5nTKAKQ=="
INFLUX_ORG = "MC"

INFLUX_BUCKET = "telemetry"


def generate_random_data():
    
    id = "L1.0_B"
    altitude = uniform(0, 500)  # in meters
    temperature = uniform(10, 40)  # in Celsius
    humidity = uniform(20, 80)  # in percentage
    timestamp = dt.datetime.now(pytz.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")

    data = {
        "measurement": "L1B",
        "tags": {
            "drone_id": id
        },
        "fields": {
            "altitude": altitude,
            "temperature": temperature,
            "humidity": humidity
        },
        "time": timestamp
    }

    return data


    
if __name__=="__main__":
    
    # Create your client
    client = InfluxDBClient(url=INFLUX_URL, org=INFLUX_ORG ,token=INFLUX_TOKEN)
    write_api = client.write_api(write_options=SYNCHRONOUS)
    
    while 1:
        try:
            data = generate_random_data()
            
            write_api.write(bucket=INFLUX_BUCKET, record=data)
            
            print('successfully inserted new data point')
            
            time.sleep(0.25)
            
        except KeyboardInterrupt:
            print('Closing connection')
            write_api.__del__()
            client.__del__()
            
            break