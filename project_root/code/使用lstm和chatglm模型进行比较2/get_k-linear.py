import csv

error_value = 0.0000001
def equal(x,y):
    if abs(x - y) <= error_value :
        return True
    else:
        return False
def more_than(x,y):
    if x - y > error_value:
        return True
    else:
        return False

def little_than(x,y):
    if x - y < -error_value:
        return True
    else:
        return False

def analyze_candlestick(open_price, close_price, high_price, low_price):
    if more_than(open_price,close_price):
        if equal(high_price,open_price) and equal(low_price,close_price):
            return 1
        elif equal(high_price,open_price) and little_than(low_price,close_price):
            return 2
        elif more_than(high_price,open_price) and little_than(low_price,close_price):
            return 3
        elif more_than(high_price,open_price) and equal(low_price,close_price):
            return 4

    if little_than(open_price,close_price):
        if equal(high_price,close_price) and equal(low_price,open_price):
            return 5
        elif equal(high_price,close_price) and little_than(low_price,open_price):
            return 6
        elif more_than(high_price,close_price) and little_than(low_price,open_price):
            return 7
        elif more_than(high_price,close_price) and equal(low_price,open_price):
            return 8


    if equal(open_price,close_price):
        if equal(high_price,open_price) and equal(low_price,close_price):
            return 9
        elif equal(high_price,open_price) and little_than(low_price,close_price):
            return 10
        elif more_than(high_price,open_price) and little_than(low_price,close_price):
            return 11
        elif more_than(high_price,open_price) and equal(low_price,close_price):
            return 12
    print("error")
    return 0

def get_stocks(input_file):
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)  # 使用DictReader来读取CSV文件的每一行
        opens = [] #开盘价格
        lows  = [] # 最低价格
        highs = [] # 最高价格
        closes = [] # 收盘价格
        for row in reader:
            # 提取你感兴趣的列数据，例如'open'和'close'
            opens.append(float(row['开盘']))
            closes.append(float(row['收盘']))
            highs.append(float(row['最高']))
            lows.append(float(row['最低']))
            # print(row['开盘'],row['收盘'],row['最高'],row['最低'])
        return opens,closes,highs,lows


def write_data(output_file,title,result):
    # 打开CSV文件并写入数据
    with open(output_file, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([title])  # 写入列标题
        for item in result:
            csv_writer.writerow([item])  # 写入每个数据项

#    print("CSV文件已创建：", output_file)
    

count = [0,0,0,0,0,0,0,0,0,0,0,0]

def total(input_file,output_file):
    d1,d2,d3,d4 = get_stocks(input_file)
    result = []
    for a,b,c,d in zip(d1,d2,d3,d4):
        n = analyze_candlestick(a,b,c,d)
        if n == 0:
            print(input_file,"不要了")
            return
        result.append(n) 
        count[n - 1] += 1
    print([round(i/sum(count),3) for i in count],sum(count))
    write_data(output_file,"feature",result)

import glob
file_pattern = "my_data/*.csv"
all_file = []
for file_name in glob.glob(file_pattern):
    all_file.append(file_name)

all_file = sorted(all_file)[:-1]


error_value = 0.05

#所有美股票合集
for i in all_file:
    # total(i,i[8:])
    print(i[8:])
    # print(i)
