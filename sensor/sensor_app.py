# Runner script for all modules
from load_data import load_sensor_data
from house_info import HouseInfo
import datetime

##############################
# Do not remove these two lines
# They are needed to validate your unittest
data = []
print("Sensor Data App")
##############################

# Module 1 code here:
data = load_sensor_data()
print(f"Loaded records: {len(data)}")

# Module 2 code here:
house_info = HouseInfo(data=data)
test_area = 1
recs = house_info.get_data_by_area(field="id", rec_area=test_area)
print(f"\nHouse sensor records for area {test_area} = {len(recs)}")

test_date = datetime.datetime.strptime("5/9/20", "%m/%d/%y")
recs = house_info.get_data_by_date(field="id", rec_date=test_date)
print("\nHouse sensor records for date: {} = {}".format(test_date, len(recs)))

# Module 3 code here:

# Module 4 code here:

# Module 5 code here:
