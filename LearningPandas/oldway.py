print("Hello Pandas")
with open("weather_data.csv") as data_file:
    data= data_file.readline()
    print (data)

import csv

with open("weather_data.csv") as csv_file:
    data= csv.reader(csv_file)
    for row in data:
        print (row)