import json
import csv

file_name = "filter_data/AAAU.csv"

def get_data(file_name):
    data = []
    file = []
    with open(file_name,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data.append(row[0])
    data = data[1:]
    for i in range(0,len(data) - 25):
        file.append(data[i:i + 26])
    return file

file = get_data(file_name)
print(file[-1])
print(len(file[-1]))



