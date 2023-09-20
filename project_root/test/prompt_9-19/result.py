import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
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


#准备一个函数，输入文件名，输出预测结果，且按照训练的结果，就单个得了，反正结果也很一般
def get_visial(files,number):
    # 打开CSV文件并读取内容
    data = []
    for i in files:
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
    print("temp")
    samples = [[ int(num[0]) for num in element] for element in  samples]
    labels = [int(num[0]) for num in labels]

    #分成测试样本和训练样本
    midium = int(len(samples) * 0.8)
    train_samples = samples[:midium]
    train_labels = labels[:midium]
    test_samples = samples[midium:]
    test_labels = labels[midium:]

    # 使用Tokenizer将文本转换为整数序列
    max_words = 13  # 限制词汇表的大小
    tokenizer = Tokenizer(num_words=max_words)

    # 使用to_categorical将整数序列转换为one-hot编码
    one_hot_data = tokenizer.sequences_eto_matrix(train_samples, mode='binary')

    # 使用to_categorical将整数标签转换为one-hot编码
    one_hot_labels = to_categorical(train_labels,num_classes=max_words)

    #用t-SNE对数据降维度
    tsne = TSNE(n_components=2, random_state=42)
    data_2d = tsne.fit_transform(one_hot_data)

    # 创建一个散点图来可视化数据
    plt.scatter(data_2d[:, 0], data_2d[:, 1])
    plt.title("t-SNE Visualization of One-Hot Encoded Data")
    plt.xlabel("Dimension 1")
    plt.ylabel("Dimension 2")
    name  = str(number) + ".png"
    plt.savefig(name)

#提取某文件的股票的信息
file_pattern = "stock_American_map/*.csv"
all_file = []
for file_name in glob.glob(file_pattern):
    print(file_name)
    all_file.append(file_name)
all_file = sorted(all_file)[:-1]


files = all_file[0:500]

# files = [[i] for i in files]
files = [files]
#主函数
sum = 0
for i in files[0:]:
    sum += 1
    print(sum)
    print(i)
    get_visial(i,sum)

