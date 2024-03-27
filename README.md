# Storage and Monitoring Solution

Ideal for storing and visualising time series data in real-time from any devices connected to the internet

## Dependencies

*Docker

## Building and Running

The docker compose command is used:
```
sudo docker compose up -d
```

Log into InfluxDB: http://localhost:8086  
Log into Grafana: http://localhost:3000


Docker volumes are used so that data is not lost when the containers are shut down.
```
sudo docker compose down
```