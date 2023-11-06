from flask import Flask, request, jsonify
from pysondb import db
import socket

app = Flask(__name)

db = db.getDb("./data.json")

def listen_data():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))

    server_socket.listen(5)

    print(f"Listening on {host}:{port}")

    for x in range(1000):
        client_socket, client_address = server_socket.accept()

        print(f"Accepted connection from {client_address}")

        data = client_socket.recv(1024)
        if not data:
            break

        print(f"Received data: {data.decode('utf-8')}")

        client_socket.close()

server_socket.close()

@app.route('/', methods=['GET'])
def list_links():
    endpoints = [
        {"path": "/", "method": "GET", "description": "List all available endpoints"},
        {"path": "/data", "method": "POST", "description": "Add data to the database"},
        {"path": "/graph/<aqi-sensor-id>", "method": "GET", "description": "Visualize data for a specific AQI sensor"},
    ]
    return jsonify({"endpoints": endpoints})

@app.route('/data', methods=['POST'])
def add_data():
    data = request.json

    db.data.append(data)
    db.dump()

    return jsonify({"message": "Data added successfully!"})

@app.route('/graph/<aqi_sensor_id>', methods=['GET'])
def visualize_data(aqi_sensor_id):
    data = [entry for entry in db.data if entry.get("sensor_id") == aqi_sensor_id]

    if not data:
        return jsonify({"message": "No data available for this sensor"})

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

