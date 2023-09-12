import json
import matplotlib.pyplot as plt

#data_file = "after_decode.txt"
#data_file = "before_decode.txt"
data_file = "data/01.txt"

def file_name(data_file):
    y1 = []
    y2 = []
     # 打开文本文件并逐行读取数据
    with open(data_file, 'r') as file:
        for line in file:
            data = line.strip()  # 去除行尾的空白字符
            labels = data.split(": ")[1][1:-12].split(",")[0]  # 提取labels的值
            predict = data.split(": ")[2][1:-2].split(",")[0]  # 提取predict的值
            y1.append(float(labels))
            y2.append(float(predict))
    return y1, y2

# 示例数据





def get_pic(data_file,num):
    y1,y2=file_name(data_file)
    #计算误差率
    length = len(y1)
    sum = 0
    for i in range(0,length):
        if y1[i] == y2[i]:
            sum += 1
    print("correct:",sum / length)
    y1 = y1[:num]
    y2 = y2[:num]
    x = range(len(y1))
    

    # 创建一个图表和子图
    fig, ax = plt.subplots()

    # 绘制第一个折线图
    ax.plot(x, y1, label='ground truth')

    # 绘制第二个折线图
    ax.plot(x, y2,label='chatglm predict', linestyle='dashed')

    # 添加标题、坐标轴标签和图例
    ax.set_title('chatglm prediction comparison chart')
    ax.set_xlabel('step')
    ax.set_ylabel('predict value')
    ax.legend()  # 显示图例

    # 显示图形
    result_name = data_file[5:-4]+".png"
    plt.savefig(result_name)


def get_pic(data_file,y1,y2,num):
    y1 = y1[:num]
    y2 = y2[:num]
    x = range(len(y1))
    
    # 创建一个图表和子图
    fig, ax = plt.subplots()

    # 绘制第一个折线图
    ax.plot(x, y1, label='ground truth')

    # 绘制第二个折线图
    ax.plot(x, y2,label='transformer predict', linestyle='dashed')

    # 添加标题、坐标轴标签和图例
    ax.set_title('transformer prediction comparison chart')
    ax.set_xlabel('step')
    ax.set_ylabel('predict value')
    ax.legend()  # 显示图例

    # 显示图形
    result_name = "data.png"
    plt.savefig(result_name)


all_file = ["data/01.txt","data/02.txt","data/07.txt","data/08.txt","data/25.txt","data/42.txt"]
# for file in all_file:
#     get_pic(file,50)





# 指定要读取的 JSON 文件路径
txt_file_path = "data/data.json"

# 打开 JSON 文件以读取数据
with open(txt_file_path, 'r') as json_file:
    # 使用 json.load() 函数将 JSON 文件的内容加载为 Python 字典对象
    loaded_data_dict = json.load(json_file)

# 现在，loaded_data_dict 包含了 JSON 文件中的数据
# 你可以通过键来访问其中的列表
list1 = loaded_data_dict['list1']
list2 = loaded_data_dict['list2']

get_pic(txt_file_path,list1,list2,50)




