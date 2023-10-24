import json
import csv

#获取相应的数据集(得到“26然后总的长度”)
file_name = "filter_data/AAAU.csv"

number_to_letter = {
    '1': 'A',
    '2': 'B',
    '3': 'C',
    '4': 'D',
    '5': 'E',
    '6': 'F',
    '7': 'G',
    '8': 'H',
    '9': 'I',
    '10': 'J',
    '11': 'K',
    '12': 'L'
}

letter_to_number = {
    'A': '1',
    'B': '2',
    'C': '3',
    'D': '4',
    'E': '5',
    'F': '6',
    'G': '7',
    'H': '8',
    'I': '9',
    'J': '10',
    'K': '11',
    'L': '12'
}


def get_data(file_name,length,pred_len):
    data = []
    file = []
    with open(file_name,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data.append(number_to_letter.get(row[0]))
    data = data[1:]
    for i in range(0,len(data) - length - pred_len):
        temp = data[i:i + length + pred_len]
        merge_list = [temp[i] + temp[i + 1] for i in range(0,len(temp),pred_len)]
        file.append(merge_list)
    return file,len(file)

def get_datas(file_names,length,pred_len):
    file = []
    data = []
    for file_name in file_names:
        with open(file_name,'r') as csvfile:
            csvreader = csv.reader(csvfile)
            judge = True
            for row in csvreader:
                if judge:
                    judge = False
                    continue
                data.append(number_to_letter.get(row[0]))
    for i in range(0,len(data) - length - pred_len):
        temp = data[i:i + length + pred_len]
        merge_list = [temp[i] + temp[i + 1] for i in range(0,len(temp),pred_len)]
        file.append(merge_list)
    return file,len(file)
