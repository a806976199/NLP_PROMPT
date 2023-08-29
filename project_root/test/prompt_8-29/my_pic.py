import json
import matplotlib.pyplot as plt

#data_file = "after_decode.txt"
#data_file = "before_decode.txt"
data_file = "data/tan-initial.txt"
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
# x = [1, 2, 3, 4, 5]
# y1 = [5, 7, 2, 8, 6]
# y2 = [3, 6, 4, 9, 2]

# y1 = [i / 10000000.0 for i in y1]
# y2 = [i / 10000000.0 for i in y2]
# print(y1)
# print(y2)
def get_pic(data_file):
    y1,y2=file_name(data_file)
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


def get_pic3(data_file):
    list1,list2=file_name(data_file)
    x = range(len(list1))
    mylist = []
    for i,j in zip(list1,list2):
        if i == j:
            mylist.append(0)
        else:
            mylist.append(1)
    list1 = mylist
    plt.clf()  # 清除之前的图形
    # 绘制柱状图
#    plt.bar(x, list1, width=0.4, label='ground truth')
#    plt.bar([i + 0.4 for i in x], list2, width=0.4, label='chatglm predict')

    plt.bar(x, list1,width=1, label='ground truth')
    # 添加标签和标题
    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.title('Comparison between ground truth and chatglm predict')
    #plt.xticks([i + 0.2 for i in x], x)  # 设置x轴刻度标签
    #plt.legend()  # 添加图例

    # 显示图形
    # plt.show()
    result_name = data_file[5:-4]+".png"
    plt.savefig(result_name)

def get_pic2(data_file):
    list1,list2=file_name(data_file)
    x = range(len(list1))
    sum = 0
    for i,j in zip(list1,list2):
        if i == j:
            sum += 1
    trans = str(round(sum / len(list1),4))
    plt.clf()  # 清除之前的图形
    # 绘制柱状图
    plt.bar(x, list1, width=0.4, label='ground truth')
    plt.bar([i + 0.4 for i in x], list2, width=0.4, label='chatglm predict:'+trans)

    # 添加标签和标题
    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.title('Comparison between ground truth and chatglm predict')
    #plt.xticks([i + 0.2 for i in x], x)  # 设置x轴刻度标签
    plt.legend()  # 添加图例

    # 显示图形
    # plt.show()
    result_name = data_file[5:-4]+".png"
    plt.savefig(result_name)




# y1,y2=file_name(data_file)

# x = range(len(y1))    

# # 创建一个图表和子图
# fig, ax = plt.subplots()

# # 绘制第一个折线图
# ax.plot(x, y1, label='折线图1')

# # 绘制第二个折线图
# ax.plot(x, y2, label='折线图2', linestyle='dashed')

# # 添加标题、坐标轴标签和图例
# ax.set_title('多个折线图示例')
# ax.set_xlabel('X轴')
# ax.set_ylabel('Y轴')
# ax.legend()  # 显示图例

# # 显示图形
# plt.show()
#file_list=['data/tan-initial.txt','data/tan-result.txt','data/linear-initial.txt','data/linear-result.txt','data/tan_before_decode.txt','data/linear_before_decode.txt','data/after_decode.txt','data/no_revin.txt']

file_list=['data/1.txt','data/02.txt','data/03.txt','data/04.txt','data/05.txt','data/06.txt']

for name in file_list:
    get_pic2(name)
    
#get_pic2(data_file)
