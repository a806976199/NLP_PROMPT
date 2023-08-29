import csv

def analyze_candlestick(open_price, close_price, high_price, low_price):
    if open_price > close_price:
        if high_price > open_price and low_price < close_price:
            return 1
        elif high_price > open_price and low_price == close_price:
            return 2
        elif high_price == open_price and low_price < close_price:
            return 3
        else:
            return 4
    if open_price < close_price:
        if high_price > close_price and low_price < open_price:
            return 5
        elif high_price > close_price and low_price == open_price:
            return 6
        elif high_price == close_price and low_price < open_price:
            return 7
        else:
            return 8
    else:
        if high_price > open_price and low_price < open_price:
            return 9
        elif high_price > open_price and low_price == open_price:
            return 10
        elif high_price == open_price and low_price < open_price:
            return 11
        else:
            return 12


def get_stocks(input_file):
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)  # 使用DictReader来读取CSV文件的每一行
        opens = [] #开盘价格
        lows  = [] # 最低价格
        highs = [] # 最高价格
        closes = [] # 收盘价格
        for row in reader:
            # 提取你感兴趣的列数据，例如'open'和'close'
            opens.append(float(row['open']))
            closes.append(float(row['close']))
            highs.append(float(row['high']))
            lows.append(float(row['low']))        
        return opens,closes,highs,lows


def write_data(output_file,title,result):
    # 打开CSV文件并写入数据
    with open(output_file, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([title])  # 写入列标题
        for item in result:
            csv_writer.writerow([item])  # 写入每个数据项

    print("CSV文件已创建：", output_file)
    



def total(input_file,output_file):
    d1,d2,d3,d4 = get_stocks(input_file)
    result = []
    for a,b,c,d in zip(d1,d2,d3,d4):
       result.append(analyze_candlestick(a,b,c,d)) 
    write_data(output_file,"feature",result)

total("stock/000001.csv","output.csv")

import glob
file_pattern = "stock/*.csv"
all_file = []
for file_name in glob.glob(file_pattern):
    print(file_name)
    all_file.append(file_name)

all_file = sorted(all_file)[:-1]

  
for i in all_file:
    total(i,i[6:])
