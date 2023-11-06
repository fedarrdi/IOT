#  Значи това е програмата която симулира сензорите , тя праща някъв json file на някъв URL който трябва да прочетеш ти
#  Има още една програма  test.py тя симулира нещо като това което ти трябва да напишеш 
#  Тя слуша на някъв порт и принита ти само трябва да го визуализираш
#  Dokerfile лесно се пише може да кажеш на chatgpt
#  Ако искаш да видиш как работят програмите в един терминал пускаш python test.py
#  В друг пускаш python app.py те ще си комуникират само трябва да визуализраш и да слагаш в база данни нещата
#  
import threading
import time
import random
import requests

def simulate_sensor(sensor_id, server_url):
    while True:
        time.sleep(1)
        
        data = {
            "sensor_id": sensor_id,
            "timestamp": time.time(),
            "value": random.uniform(0, 100)
        }

        try:
            response = requests.post(server_url, json=data)

            if response.status_code == 200:
                print(f"Sensor {sensor_id} sent data: {data}")
            else:
                print(f"Error sending data from sensor {sensor_id}: {response.status_code}")

        except Exception as e:
            print("ERROR")

num_sensors = 3
container_url = "http://localhost:8000/data_endpoint"

threads = []

for sensor_id in range(num_sensors):
    thread = threading.Thread(target=simulate_sensor, args=(sensor_id, container_url))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
