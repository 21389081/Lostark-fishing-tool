import random
import time
import requests

Function to generate random values
def generate_random_values():
    voltage = float(round(random.uniform(100, 240), 2))  # Voltage range from 100V to 240V
    wattage = float(round(random.uniform(0, 500), 2))    # Wattage range from 0W to 500W
    current = float(round(random.uniform(0, 10), 2))    # Current range from 0A to 10A
    return voltage, wattage, current

Number of times to run the loop
num_iterations = 300

print("Generating data...")

Node-RED URL
node_red_url = "http://127.0.0.1:1880/data"

Loop to generate data num_iterations times
for i in range(num_iterations):
    try:
        voltage, wattage, current = generate_random_values()
        data = {
            "voltage": voltage,
            "wattage": wattage,
            "current": current
        }
        print(f"Iteration {i+1}: Sending data: {data}")
        response = requests.post(node_red_url, json=data)
        float(response)
        print(f"Response status code: {response.status_code}")
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            print(f"Response content: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    time.sleep(3)  # Sleep for 3 seconds before generating new values

print("Data generation completed.")