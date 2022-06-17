import csv
import pandas as pd

data=[]

with open("stars.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data.append(row)
      
headers=data[0]
stars_data=data[1:]


for datapoint in stars_data:
    datapoint[2]=datapoint[2].lower()
with open("Brightest.csv","a+")as f :
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(stars_data)

