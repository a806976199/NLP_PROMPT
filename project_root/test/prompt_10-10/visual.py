import json
import matplotlib.pyplot as plt
import glob

data_file = "data/01.txt"

#获取chatglm预测结果的数据
def get_chatglm_predict(data_file):
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

#获取lstm预测结果的数据
def get_lstm_predict(data_file):
    y1 = []
    y2 = []
    with open(data_file,"r") as my_file:
        data = json.load(my_file)
        print(data['predict'])
        y1 = [float(num) for num in data['labels']]
        y2 = [float(num) for num in data['predict']]
    return y1,y2

# 示例数据
def get_pic_chatglm(data_file,num):
    y1,y2=get_chatglm_predict(data_file)
    #计算误差率
    length = len(y1)
    sum = 0
    for i in range(0,length):
        if y1[i] == y2[i]:
            sum += 1
    correct =round(sum / length,4)
    # print("correct:",sum / length)
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
    # print("chatglm_error:",round(sum / length,4))
    ax.set_title('chatglm prediction comparison chart:'+str(round(sum / length,4)))
    ax.set_xlabel('step')
    ax.set_ylabel('predict value')
    ax.legend()  # 显示图例

    # 显示图形
    # result_name = lstm_file[10:-5]+"_chatglm.png"
    # result_name = data_file[13:-4]+"_chatglm.png"
    # plt.savefig(result_name)
    return correct

def get_pic_lstm(data_file,num):
    y1,y2=get_lstm_predict(data_file)
    #计算误差率
    length = len(y1)
    sum = 0
    for i in range(0,length):
        if y1[i] == y2[i]:
            sum += 1
    correct =round(sum / length,4) 
    # print("correct:",sum / length)
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
    # print("lstm_error:",round(sum / length,4))
    ax.set_title('transformer prediction comparison chart'+str(round(sum / length,4)))
    ax.set_xlabel('step')
    ax.set_ylabel('predict value')
    ax.legend()  # 显示图例

    # 显示图形

    # result_name = data_file[10:-5] + "_lstm.png"
    # plt.savefig(result_name)
    return correct,data_file[11:-5]


file_a = "lstm_data/AAAU.json"
file_b = "chatglm_data/1.txt"

#得到那个卷积模型的最终结果
'''
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

# 得到那个其他的结果

for i in range(1,30):
    name = 'data/'+str(i)+'.txt'
    get_pic_chatglm(name,40)



number = 350
#得到lstm文件内所有股票文件
file_pattern = "lstm_data/*.json"
file_pattern2 = "chatglm_data/*.txt"
lstm_file = []
chatglm_file = []
for file_name in glob.glob(file_pattern):
    lstm_file.append(file_name)
for file_name in glob.glob(file_pattern2):
    chatglm_file.append(file_name)
lstm_file,chatglm_file = sorted(lstm_file),sorted(chatglm_file)
lstm_file = lstm_file[:number + 1]
chatglm_file = chatglm_file[:number + 1]


lstm_correct = []
chatglm_correct = []
names = []

for lstm,chatglm in zip(lstm_file,chatglm_file):
    lstm_correct.append(get_pic_lstm(lstm,40)) 
    chatglm_correct.append(get_pic_chatglm(chatglm,40,lstm))
    names.append(lstm[10:-5])

for i in range(0,number):
    print(names[i],"序号：",i,",error_lstm:",lstm_correct[i],"error_chatglm",chatglm_correct[i])
'''


# 得到lstm里面的所有文件:
average_lstm_correct = 0
lstm_correct = dict()
lstm_correct['name'] = []
lstm_correct['correct'] = []
file_pattern = "initial_25/*.json"
lstm_file = []
for file_name in glob.glob(file_pattern):
    lstm_file.append(file_name)
lstm_file = sorted(lstm_file)
numbers = len(lstm_file)
print(numbers)
for file in lstm_file:
    x,y = get_pic_lstm(file,40)
    lstm_correct['name'].append(y)
    lstm_correct['correct'].append(x)
    average_lstm_correct += lstm_correct['correct'][-1]
    print(lstm_correct)
save_file = "initial_25.json"
with open(save_file,'w') as file:
    json.dump(lstm_correct,file)

print("mse:",average_lstm_correct / len(lstm_file))

'''
# 得到chatglm训练的文件数据结果
average_chatglm_correct = 0
chatglm_correct = dict()
chatglm_correct['name'] = []
chatglm_correct['correct'] = []
file_pattern = "chatglm_data/*.txt"
chatglm_file = []
for file_name in glob.glob(file_pattern):
    chatglm_file.append(file_name)
chatglm_file = sorted(chatglm_file)
print(chatglm_file)
print(len(chatglm_file))

#获得指标结果
load_list = []
with open("index.json",'r') as index:
    load_list = json.load(index)

index = 0
for file in chatglm_file:
    chatglm_correct['correct'].append(get_pic_chatglm(file,40))
    chatglm_correct['name'].append(load_list[index])
    average_chatglm_correct += chatglm_correct['correct'][-1]
    index += 1
with open("chatglm_25.json",'w') as file:
    json.dump(chatglm_correct,file)

print("mse:",average_chatglm_correct / len(chatglm_file))
'''
