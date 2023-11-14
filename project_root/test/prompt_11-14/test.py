def get_dict(file_name):
    # 打开文件
    res = dict()
    all_data = []
    with open(file_name, 'r') as file:
        # 逐行读取数据
        i = 1
        for line in file:
            # 处理每一行数据
            processed_line = line.strip()  # 去除首尾的空白字符
            # 进行其他的处理操作，根据具体需求进行编写
            all_data.append(processed_line)
            # 打印处理后的数据
            # print(processed_line)

    for i in range(0,len(all_data),2):
        if all_data[i][:3] == "mse":
            # 分割字符串
            key_value_pairs = all_data[i].split(", ")
            
            # 创建空字典
            result_dict = {}
        
            # 解析每个键值对
            for pair in key_value_pairs:
                key, value = pair.split(":")
                result_dict[key.strip()] = float(value)
        
            res[all_data[i + 1]]=result_dict

    # print(res)
    return res

feature_1=get_dict('feature_1.txt')
feature_11=get_dict('feature_11.txt')
no_feature_1=get_dict('no_feature_1.txt')
no_feature_11=get_dict('no_feature_11.txt')
key_list = list(feature_1.keys())
print(key_list)

#准备画图就完事了.

import matplotlib.pyplot as plt

def plot_stock(number,error_type,title):
    #获得数据
    feature_1_list = list(feature_11.values())
    no_feature_1_list = list(no_feature_11.values())

    list1 =[i[error_type] / 10 for i in feature_1_list]
    list2 = [i[error_type] / 10 for i in no_feature_1_list]
    #进行计算大小比例
    sum = 0
    for x,y in zip(list1,list2):
        if x < y:
            sum += 1
    rate = sum / len(list1)
    rate = round(rate,4)
    # 准备数据
    x = [i for i in range(1,number + 1)]
    y1 = list1[:number]
    y2 = list2[:number] 

    # 绘制第一条折线
    plt.plot(x, y1, label='extra_feature')

    # 绘制第二条折线
    plt.plot(x, y2, label='normal')

    # 添加标题和坐标轴标签
    plt.title(title +',rate:'+ str(rate))
    plt.xlabel('stock_type')
    plt.ylabel(error_type)

    # 添加图例
    plt.legend()
    photo_name = title+'.png'
    plt.savefig(photo_name)
    # 显示图形
    plt.show()
    print(rate)
    return rate

plot_stock(300,'mae','compare_feature')
