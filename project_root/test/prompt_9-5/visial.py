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

def get_result(files,numbers):
    start,list1 = file_name(files[0])
    _,list2 = file_name(files[1])
    _,list3 = file_name(files[2])
    _,list4 = file_name(files[3])
    _,list5 = file_name(files[4])
    # list1,list2=file_name(data_file)
    plt.clf()  # 清除之前的图形
    # # 绘制柱状图
    # plt.bar(x, list1, width=0.4, label='ground truth')
    # plt.bar([i + 0.4 for i in x], list2, width=0.4, label='chatglm predict:'+trans)
    # 绘制折线图
    list1 = list1[-numbers:]
    list2 = list2[-numbers:]
    list3 = list3[-numbers:]
    list4 = list4[-numbers:]
    list5 = list5[-numbers:]
    start = start[-numbers:]
    plt.plot(start,label='ground truth', marker='o', linestyle='-', color='b')
    plt.plot(list1,label='chatglm predict', marker='p', linestyle='--', color='g')
    plt.plot(list2,label='DLinear predict', marker='x', linestyle='--', color='m')
    plt.plot(list3,label='AutoFormer predict', marker=',', linestyle='--', color='y')
    plt.plot(list4,label='Informer predict', marker='<', linestyle='--', color='c')
    plt.plot(list5,label='Transformer predict', marker='>', linestyle='--', color='k')

    # 添加标签和标题
    plt.xlabel('step')
    plt.ylabel('predict value')
    plt.title('chatglm prediction comparison chart')
    #plt.xticks([i + 0.2 for i in x], x)  # 设置x轴刻度标签
    plt.legend()  # 添加图例

    # 显示图形
    result_name = files[0][5:-4]+".png"
    print(result_name)
    plt.savefig(result_name)
    # plt.show()



numbers = 40
file_nums = ["01","02","03","04","05","06"]

file_num = "01"

file_stock = "data/stock-much/0000"
Linear="_16_4_DLinear_custom_ftM_sl16_ll4_pl4_dm512_nh8_el2_dl1_df2048_fc1_ebtimeF_dtTrue_Exp_0/output.txt"
AutoFormer="_ili_36_4_Autoformer_custom_ftM_sl16_ll4_pl4_dm512_nh8_el2_dl1_df2048_fc3_ebtimeF_dtTrue_Exp_0/output.txt"
Informer="_ili_36_4_Informer_custom_ftM_sl16_ll4_pl4_dm512_nh8_el2_dl1_df2048_fc3_ebtimeF_dtTrue_Exp_0/output.txt"
Transformer="_ili_36_4_Transformer_custom_ftM_sl16_ll4_pl4_dm512_nh8_el2_dl1_df2048_fc3_ebtimeF_dtTrue_Exp_0/output.txt"
models=[Linear,AutoFormer,Informer,Transformer]


def result(file_nums):
    for file_num in file_nums:
        files=[]
        input_file = "data/" + file_num+".txt"
        files.append(input_file)
        for model in models:
            name = file_stock + file_num + model
            files.append(name)
        print(files)
        get_result(files,numbers)

result(file_nums)
