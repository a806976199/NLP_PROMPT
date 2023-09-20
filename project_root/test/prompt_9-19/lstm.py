import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Embedding, Dense
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
import json
import random
import csv
import glob
import matplotlib.pyplot as plt


#准备一个函数，输入文件名，输出预测结果，且按照训练的结果，就单个得了，反正结果也很一般
def get_predict(files):
    # 打开CSV文件并读取内容
    data = []
    for i in files:
        print(i)
        with open(i, 'r',newline="") as csvfile:
            csvreader = csv.reader(csvfile)
            # 如果CSV文件的第一行包含标题行，请跳过它
            next(csvreader, None)
            # 遍历CSV文件的每一行并将其添加到data列表中
            for row in csvreader:
                data.append(row)

    #得到样本数据
    samples = []
    labels = []
    length = 20

    for i in range(0,len(data) - length):
        temp = []
        for j in range(0,length) :
            temp.append(data[j + i][-1])
        samples.append(temp)
        labels.append(data[i + length])

    samples = [[ int(num[0]) for num in element] for element in  samples]
    labels = [int(num[0]) for num in labels]

    #获得每种分类的比例
    # count = [0] * 13
    # for i in data:
    #     count[int(i[0])] += 1
    # count = [round(i / len(data),4) for i in count]
    # print(file_name[-1],count)

    #分成测试样本和训练样本
    midium = int(len(samples) * 0.8)
    train_samples = samples[:midium]
    train_labels = labels[:midium]
    test_samples = samples[midium:]
    test_labels = labels[midium:]

    # 设置相同的随机种子以确保两个列表的随机性相同
    # random_seed = 42
    # random.seed(random_seed)
    # random.shuffle(train_labels)
    # random.shuffle(train_samples)

    # 使用Tokenizer将文本转换为整数序列
    max_words = 13  # 限制词汇表的大小
    tokenizer = Tokenizer(num_words=max_words)

    # 使用to_categorical将整数序列转换为one-hot编码
    one_hot_data = tokenizer.sequences_to_matrix(train_samples, mode='binary')

    # 使用to_categorical将整数标签转换为one-hot编码
    one_hot_labels = to_categorical(train_labels,num_classes=max_words)

    # 创建模型
    model = Sequential()
    model.add(Embedding(input_dim=max_words, output_dim=32, input_length=one_hot_data.shape[1]))
    model.add(LSTM(units=64, activation='relu'))
    model.add(Dense(units=max_words, activation='softmax'))  # 多类别输出

    # 编译模型
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # 训练模型
    model.fit(one_hot_data, one_hot_labels, epochs=1, batch_size=7)

    # 进行预测
    test_one_hot_data = tokenizer.sequences_to_matrix(test_samples, mode='binary')
    predictions = model.predict(test_one_hot_data)

    # 打印预测结果
    predicts = []
    for i in predictions:
        n = np.argmax(i)
        predicts.append(n)

    sum = 0        
    for i in range(0,len(predicts)):
        if test_labels[i] == predicts[i]:
            sum += 1

    print(predicts)
    print(sum/len(predicts))
    rate = round(sum / len(predicts),4)
    return test_labels,predicts,rate

#画图可视化
def get_pic(number,rate,y1,y2,num):
    if len(y1) < num:
        return
    y1 = y1[:num]
    y2 = y2[:num]
    x = range(len(y1))
    print(rate)
    # 创建一个图表和子图
    fig, ax = plt.subplots()

    # 绘制第一个折线图
    ax.plot(x, y1, label='ground truth')

    # 绘制第二个折线图
    ax.plot(x, y2,label='transformer predict', linestyle='dashed')

    # 添加标题、坐标轴标签和图例
    ax.set_title('transformer prediction comparison chart:'+str(rate))
    ax.set_xlabel('step')
    ax.set_ylabel('predict value')
    ax.legend()  # 显示图例

    # 显示图形
    result_name = str(number)+".png"
    plt.savefig(result_name)

#提取某文件的股票的信息
file_pattern = "stock_American_map/*.csv"
all_file = []
for file_name in glob.glob(file_pattern):
    print(file_name)
    all_file.append(file_name)
all_file = sorted(all_file)[:-1]

file_name = all_file[0:100]

# file_name = [[num] for num in file_name]
file_name = [file_name]
print(file_name)

#主函数
sum = 0
for i in file_name:
    sum += 1
    print(sum)
    x,y,rate = get_predict(i)
    get_pic(sum,rate,x,y,40)

