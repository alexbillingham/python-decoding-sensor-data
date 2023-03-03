import os
import glob
import csv

sensor_data = []


def load_sensor_data():
    # Load all csv files from datasets folder
    sensor_files = glob.glob(os.path.join(os.getcwd(), "datasets", "*.csv"))

    # Loop sensor files and add to the sensor data list
    for sensor_file in sensor_files:
        with open(sensor_file) as data_file:
            data_reader = csv.DictReader(data_file, delimiter=",")
            for row in data_reader:
                sensor_data.append(row)

    return sensor_data


if __name__ == "__main__":
    load_sensor_data()
