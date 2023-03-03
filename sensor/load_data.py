import os
import glob
import csv

sensor_data = []


def load_sensor_data():
    # Load all csv files from datasets folder
    sensor_files = glob.glob(os.path.join(os.getcwd(), "datasets", "*.csv"))
    for sensor_file in sensor_files:
        with open(file=sensor_file) as file_data:
            data_reader = csv.DictReader(file_data, delimiter=",")
            for data_row in data_reader:
                sensor_data.append(data_row)

    return sensor_data


if __name__ == "__main__":
    load_sensor_data()
