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

with open('total.json','r') as file:
    total_char = json.load(file)


#输入:几个字符
#输出:组合体
def three_char(z,y,x):
    total3 = x + y + z
    total2 = x + y
    total1 = x 
    if total3 in total_char:
        return total3
    elif total2 in total_char:
        return total2
    else:
        return total1

def sum_char(history):
    total3 = history[-3] + history[-2] + history[-1]
    total2 = history[-2] + history[-1] 
    total1 = history[-1]
    if total3 in total_char:
        return total3,0
    elif total2 in total_char:
        return total2,1
    else:
        return total1,2

res = []

def func_history(history):
    global res
    if len(history) == 0:
        return res[:]
    elif len(history) == 1:
        res.append(history[-1])
        return res[:]
    elif len(history) == 2:
        if (history[-1] + history[-2]) in total_char:
            res.append(history[-1] + history[-2])
        return res[:]
    char,num = sum_char(history[-3:])
    print(char)
    res.append(char)
    func_history(history[:-3 + num])

def func_data(history):
    stack = []
    result = []
    while len(history) != 0:
        if len(history) == 1:
            result.append(history[-1])
            history.pop()
            break;
        if len(history) == 2:
            if(history[-2] + history[-1]) in total_char:
                result.append(history[-2] + history[-1])
                break;
            else:
                result.append(history[-1])
                history.pop()
                break;
        char,num = sum_char(history[-3:])
        result.append(char)
        history = history[:-3 + num]
    return result


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
    data = func_data(data)
    
    for i in range(0,len(data) - length - pred_len):
        temp = data[i:i + length + pred_len]
        merge_list = [temp[i] for i in range(0,len(temp))]
        file.append(merge_list)
    return file,len(file)

def get_data(file_name,length,pred_len):
    data = []
    file = []
    with open(file_name,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data.append(number_to_letter.get(row[0]))
    data = data[1:]
    data = func_data(data)

    for i in range(0,len(data) - length - pred_len):
        temp = data[i:i + length + pred_len]
        merge_list = [temp[i] for i in range(0,len(temp))]
        file.append(merge_list)

    return file,len(file)
