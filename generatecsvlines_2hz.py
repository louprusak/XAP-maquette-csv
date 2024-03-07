import csv
import random
import time
from datetime import datetime, timedelta

# Generate random data
def generate_data_with_time(current_time):
    rpm = random.randint(1000, 5000)
    water_temp = random.uniform(60, 100)
    oil_temp = random.uniform(80, 120)
    gear_voltage = random.uniform(11, 14)
    return [current_time.strftime("%H:%M:%S"), rpm, water_temp, oil_temp, gear_voltage]

# Write headers of csv
def write_headers(filename, headers):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

# Write data on csv
def write_csv(filename, data):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Headers
headers = ['time', 'rpm', 'water_temp', 'oil_temp', 'gear_volt']

# CSV file name
filename = 'data_2hz.csv'

# Write headers
write_headers(filename, headers)

# Temps de départ
start_time = datetime.strptime("14:26:00", "%H:%M:%S")

# Execution duration
duration = 360 

# Data generation
i = 0
while i < duration:
    current_time = start_time + timedelta(seconds=i)
    data = generate_data_with_time(current_time)
    write_csv(filename, data)
    i += 1
    print("Add data")
    time.sleep(0.5)

print("Generate success")
