import csv
import datetime
import math
import json
import torch 


#输入我想要的序列的函数列表:
# 示例函数
def square(x):
    return x ** 2

def cube(x):
    return x ** 2 + 3

def polynomial1(x):
    return x * x - 2 * x + 1

def polynomial2(x):
    return x * x - 4 * x + 4

def Sin(x):
    return math.sin(x)

def Cos(x):
    return math.cos(x)

def sqrt(x):
    return math.sqrt(x)

def Tan(x):
    return math.tan(x)

def log(x):
    return math.log(x + 1)

def tri_poly(x):
    return math.sin(x * x + 2)

def Sum(x):
    return (Sin(x) + Cos(x) + tri_poly(x)) / 3

def atan(x):
    return math.atan(x)

def linear(x):
    return x * x + x - 1 

def tan(x):
    return math.tan(x)

def generate_data(struct_num,pre_num,numbers,functions,save_file_name,read_files):
    def generate_year_sequence(year):
        start_date = datetime.date(year, 1, 1)  # 设置起始日期为给定年份的1月1日
        end_date = datetime.date(year + 1, 1, 1)  # 设置结束日期为给定年份的下一年的1月1日

        current_date = start_date
        time_sequence = []

        while current_date < end_date:
            time_sequence.append(current_date)
            current_date += datetime.timedelta(days=1)  # 递增一天

        return time_sequence



    def generate_day_sequence():
        start_time = datetime.time(0, 0, 0)  # 设置起始时间为00:00:00
        end_time = datetime.time(23,50, 0)  # 设置结束时间为23:50:00

        current_time = start_time
        time_sequence = []

        while current_time != end_time :
            time_sequence.append(current_time)
            current_time = (datetime.datetime.combine(datetime.date.today(), current_time)
                            + datetime.timedelta(minutes=10)).time()  # 递增10分钟
        time_sequence.append((datetime.datetime.combine(datetime.date.today(), time_sequence[-1])
                            + datetime.timedelta(minutes=10)).time())    
        return time_sequence

    def generate_all_sequence():
        # 输入年份
        # year = int(input("请输入年份："))
        year = 2021
        # 生成时间序列
        date_sequence = generate_year_sequence(year)

        # 生成时间序列
        time_sequence = generate_day_sequence()
        
        res = []
        # 输出时间序列
        for date in date_sequence:
            for time in time_sequence:
                date_str = str(date)
                time_str = str(time.strftime("%H:%M:%S"))
                res.append(date_str+' '+ time_str)

        return res        

    def evaluate_functions(functions, x, n):
        """
        求解器函数，输入多个函数和一个值 x，输出每个函数在 x 处的结果。
        """
        result = ''
        for func in functions:
            result += ',' + str(round(func(x),n))
        return result


    #temp
    def write_csv(filename):
        # 打开CSV文件进行写入
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # 输入表头
            # header = input("请输入表头（以逗号分隔）：")
            # head = 'date,value,'
            head = 'value,'
            for name in functions:
                head += name.__name__ + ','
#            head = head[:-1]
            writer.writerow(head.split(','))

            # 输入数据行，直到输入空行为止
            # while True:
            #     data = input("请输入数据行（以逗号分隔），或者输入空行退出：")
            #     if not data:
            #         break
            #     writer.writerow(data.split(','))
            
            time = generate_all_sequence()
            
            for i in range(numbers):
                # data = input("请输入数据行（以逗号分隔），或者输入空行退出：")
                # data = time[i] +  ',' + str(i) + evaluate_functions(functions,i)
                data = str(i) + evaluate_functions(functions,i,4)
                writer.writerow(data.split(','))

        print("CSV文件写入完成！")

    #将一个序列变成一个合理的指示json文件
    def generate_dataset(Instructions,Inputs,Outputs):
        data = []
        
        for Instruction,Input,Output in zip(Instructions,Inputs,Outputs):
            entry = {
                "Instruction": Instruction,
                "Input": Input,
                "Output": Output
            }
            data.append(entry)

        return data

    #csv数据的文件名字+路径,按照顺序进行读取数据,但是不重复读取数据，如果要重复读取也可以改变每次初始输入的值
    def get_data(file_name,pre_num,struct_num):
        inputs = []
        outputs = []
        text = ""
        index = ""
        indexs = []
        struct_num += 1
        # 打开文件并逐行读取数据
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                else:
                    i = i % (pre_num + struct_num + 1)
                    line = ','.join(row) # 将每行数据用逗号连接起来
                    text += line + ',#,'  # 添加换行符
                    split_values = line.split(",")  # 使用逗号分割字符串
                    index += split_values[-1] +',' # 提取第3个元素
                    if i == (struct_num - 1):
                        text = text[:-1]
                        inputs.append(text)
                        text = ""
                        index = ""
                    if i == (pre_num + struct_num - 1):
                        index = index[:-1]
                        outputs.append(index)
                        index = ""
        return inputs,outputs

    #也可以使用这种方式获得新的数据，这种方式可以通过获得各种随机组合的例子。
    def get_data_test(file_name,pre_num,struct_num):
        inputs = []
        outputs = []
        Input=""
        Output=""

        data = []
        text = ""
        # 打开文件并逐行读取数据
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                    data.append(row)
            data = [[float(element) for element in sublist] for sublist in data[1:]]
            #进行输入和输出的内容授予
            for i in range(numbers - pre_num - struct_num - 1):
                x = torch.tensor(data[i:i + struct_num])
                x_revin = x
                y = torch.tensor(data[i + struct_num :i + struct_num + pre_num])
                y_revin = y
                x_revin = x_revin.T
                y_revin = y_revin.T
                # inputs.append(str(torch.reshape(x_revin.T,(-1,)))[8:-38])
                # outputs.append(str(y_revin.T[-1])[8:-29])
                x_revin = [[round(float(x), 5) for x in row] for row in x_revin]
                y_revin = [[round(float(y), 5) for y in row] for row in y_revin]
                x_str = ""
                for a in x_revin:
                    x_str += "dim:"
                    for b in a:
                        x_str += str(b) + ","
                inputs.append(x_str[:-1]+"?")
                outputs.append(str(y_revin[-1])[1:-1])
        return inputs,outputs

    def save_data(read_file,write_file,category,pre_num,struct_num):
        #Inputs,Outputs = get_data(read_file,pre_num,struct_num)
        Inputs,Outputs = get_data_test(read_file,pre_num,struct_num)
        #进行inputs,outputs长度截断,以保证两者长度相同
        if len(Inputs) < len(Outputs):
            Outputs = Outputs[:len(Inputs)]
        else:
            Inputs = Inputs [:len(Outputs)]
        # 指令的形式
        Instructions = [
            "For a {category} Time-series, from the existing ${struct_num}$ elements,predict the last column of future ${pre_num}$ elements?"
        ]
        Instructions = [instruction.format(pre_num=pre_num,struct_num=struct_num,category=category) for instruction in Instructions]
        Instructions = Instructions * len(Inputs)

        dataset = generate_dataset(Instructions,Inputs,Outputs)

        # 将数据保存到JSON文件
        formatted_data = json.dumps(dataset, indent=2)
        
        with open(write_file, 'w') as file:
            file.write(formatted_data)
        print(write_file,"文件已保存")

    train_num = 8
    total_num = 10

    # 输入要创建的CSV文件名
    filename = "test.csv"
    # 调用写入CSV的函数
    write_csv(filename)

    save_data(read_files,"test.json","test",pre_num,struct_num)

    # 读取JSON文件
    with open('test.json') as file:
        data = json.load(file)

    print("len",len(data))

    for item in data:
        #item["Combined"] = item["Instruction"] + "!!" + item["Input"]
        # 如果你想去掉最后一个逗号，可以使用下面的代码替代上面一行代码
        item["Input"] = item["Instruction"] + " " + item["Input"]

    #将一个序列变成一个合理的指示json文件
    def generate_dataset(Inputs,Outputs):
        data = []
        for Input,Output in zip(Inputs,Outputs):
            entry = {
                "content": Input,
                "summary": Output
            }
            data.append(entry)

        return data

    # 访问JSON数据
    input_data = []
    output_data = []
    dataset_train = []
    dataset_dev = []

    print("len",len(data))
    length = len(data)
    i = 0
    for item in data: 
        #这一步数据集合分成验证集合和训练集合。
        if i == int(length * train_num / total_num):
            dataset_train = generate_dataset(input_data,output_data)
            input_data = []
            output_data = []
        input_data.append(item["Input"])
        output_data.append(item["Output"])
        i = i + 1
        
    dataset_dev = generate_dataset(input_data,output_data)

    #输出文件
    write_train_file = "train.json"
    write_dev_file = "dev.json"

    # 将数据保存到JSON文件
    formatted_train_data=json.dumps(dataset_train, indent=2)
    formatted_dev_data=json.dumps(dataset_dev, indent=2)

    print("dev",len(dataset_dev))
    print("train",len(dataset_train))

    with open(write_train_file, 'w') as file:
        file.write(formatted_train_data)
    print(write_train_file,"文件已保存")
    
    with open(write_dev_file, 'w') as file:
        file.write(formatted_dev_data)
    print(write_dev_file,"文件已保存")
    

    import os
    if not os.path.exists(save_file_name):
        os.mkdir(save_file_name)
    else:
        # 文件已存在
        print('File already exists.')

    os.remove("test.json")
    os.remove("test.csv")
    import shutil
    pwd= '/home/ckj/file/temp-experience/git-experience/tool/machine_learning/my_process/T5_model/my_test/time_series_template/func_time/k-linear'
    src_file1 = pwd + '/dev.json'
    src_file2 = pwd + '/train.json'
    dest_file = pwd + '/' + save_file_name

    if not os.path.exists(dest_file+'/dev.json'):
        shutil.move(src_file1,dest_file)
    if not os.path.exists(dest_file+'/train.json'):        
        shutil.move(src_file2,dest_file)


all_functions=[
    [linear]
]

import glob
file_pattern = "stock_map/*.csv"
all_file = []
for file_name in glob.glob(file_pattern):
    print(file_name)
    all_file.append(file_name)
all_file = sorted(all_file)[:-1]

print(all_file)
for read_file in all_file:
    print(read_file[-6:-4])
#这个是数量，序列的长度
numbers = 2431

for struct_num in range(16,18,2):
     for functions in all_functions:
         for read_file in all_file:
             generate_data(int(struct_num),int(4),numbers,functions,"test"+read_file[-6:-4],read_file)
