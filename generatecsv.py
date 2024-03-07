import csv
import random
import time
from datetime import datetime, timedelta

# Generate random data
def generate_random_data(current_time):
    #current_time = time.strftime("%H:%M:%S")
    rpm = random.randint(1000, 5000)
    water_temp = random.uniform(60, 100)
    oil_temp = random.uniform(80, 120)
    gear_voltage = random.uniform(11, 14)
    return [current_time.strftime("%H:%M:%S"), rpm, water_temp, oil_temp, gear_voltage]

# Write data on csv
def write_csv(filename, data, headers):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for row in data:
            writer.writerow(row)

# Rows to generate
num_rows = 100

# Start Time
start_time = datetime.strptime("14:26:00", "%H:%M:%S")

# Data generation
data = []
for _ in range(num_rows):
    data.append(generate_random_data(start_time))
    start_time += timedelta(seconds=1)

# Headers
headers = ['time', 'rpm', 'water_temp', 'oil_temp', 'gear_volt']

# Write data
write_csv('data.csv', data, headers)

print("Generate success")