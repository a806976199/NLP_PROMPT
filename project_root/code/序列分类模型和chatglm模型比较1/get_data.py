# 准备数据集
import csv
import math
import random
import glob

def get_csv(file_name,data_list):
    with open(file_name, newline='') as csvfile:
        sum = 0
        for row in csvfile:
            if sum == 0:
                sum = 1
                continue
            # 假设数据位于每一行的第一个列中
            data = float(row.strip())  # 将数据转换为整数或者适合的数据类型
            data_list.append(data)
    return data_list

def get_data(history,file_name,batch_size):
    data_list = []
    #将所有数据集都合并成一个数据集合
    file_pattern = file_name
    all_file = []
    for file_name in glob.glob(file_pattern):
        print(file_name)
        all_file.append(file_name)
    all_file = sorted(all_file)[:-1]
    # all_file = sorted(all_file)[:2]
    for csv_file in all_file:
        get_csv(csv_file,data_list)


    # 提取的数据列表
    history_data_sets = []
    labels = []
    for i in range(0,len(data_list) - history):
        history_data_sets.append(data_list[i:i+history])
        labels.append(data_list[i + history])

    
    print(len(labels))
    print(len(history_data_sets))

    #打乱整个标签顺序
    my_order = list(range(0,len(history_data_sets)))
    random.shuffle(my_order)
    history_data_sets = [history_data_sets[i] for i in my_order]
    labels = [int(labels[i]) for i in my_order]

    #对所有数据进行的几种归一化 
    history_data_sets = [[(value - 6.5) / 5.5 for value in number]  for number in history_data_sets ]
    # history_data_sets = [[(value - 1) / 12 for value in number]  for number in history_data_sets ]
    # history_data_sets = [[random.choice([0.0,1.0,0.5]) for value in number]  for number in history_data_sets ]
    # 将数据变成一个矩阵
    n = int(math.sqrt(history))
    for i in range(len(history_data_sets)):
        element = []
        for j in range(0,n):
            element.append(history_data_sets[i][j:j + n])
        history_data_sets[i] = element

    result_history = []
    result_labels = []
    for i in range(0,len(history_data_sets) - batch_size,batch_size):
        temp1 = []
        temp2 = []
        for j in range(0,batch_size):
            temp1.append(history_data_sets[i + j])
            temp2.append(labels[i + j])
        result_history.append(temp1)
        result_labels.append(temp2)

    return result_history,result_labels

# 打开CSV文件并读取数据
# 创建模型
input_dim = 64 * 1 * 1  # CNN的输出特征维度
#input_dim = 64 * 7 * 7  # CNN的输出特征维度
#input_dim = 16 * 7 * 7  # CNN的输出特征维度
hidden_dim = 256
num_classes = 13
num_layers = 2
num_heads = 4

file_name = "stock_map/*.csv"
data_list = []
history = 16
batch_size = 64
a,b=get_data(history,file_name,batch_size)
print(len(a))
print(len(b))
train_num = int(len(b) * 0.8 )
test_num = train_num + int(len(b)* 0.1 )

# 训练模型
num_epochs = 3

# 给定特定的文件组得到相应的训练结果组，直接对整体进行训练
## ==================================================###
def get_one(history,file_name,batch_size):
    data_list = []
    get_csv(file_name,data_list)

    # 提取的数据列表
    history_data_sets = []
    labels = []
    for i in range(0,len(data_list) - history):
        history_data_sets.append(data_list[i:i+history])
        labels.append(data_list[i + history])


    #打乱整个标签顺序
    my_order = list(range(0,len(history_data_sets)))
    random.shuffle(my_order)
    history_data_sets = [history_data_sets[i] for i in my_order]
    labels = [int(labels[i]) for i in my_order]
    
    copy = labels
    #对所有数据进行的几种归一化 
    history_data_sets = [[(value - 6.5) / 5.5 for value in number]  for number in history_data_sets ]

    # 将数据变成一个矩阵
    n = int(math.sqrt(history))
    for i in range(len(history_data_sets)):
        element = []
        for j in range(0,n):
            element.append(history_data_sets[i][j:j + n])
        history_data_sets[i] = element

    result_history = []
    result_labels = []
    for i in range(0,len(history_data_sets) - batch_size,batch_size):
        temp1 = []
        temp2 = []
        for j in range(0,batch_size):
            temp1.append(history_data_sets[i + j])
            temp2.append(labels[i + j])
        result_history.append(temp1)
        result_labels.append(temp2)

    return result_history,result_labels,my_order,copy

csv_history,csv_labels,my_order,my_copy = get_one(history,"stock_map/000042.csv",batch_size)

##==================================================#####


import torch
import torch.nn as nn
import torchvision
from torchvision import transforms
import torch.optim as optim
from sklearn.metrics import accuracy_score
import random
import numpy as np 

# 定义CNN用于特征提取
class CNNFeatureExtractor(nn.Module):
    def __init__(self):
        super(CNNFeatureExtractor, self).__init__()
        self.cnn = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )

    def forward(self, x):
        return self.cnn(x)

# 定义Transformer模型
class TransformerClassifier(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_classes, num_layers, num_heads):
        super(TransformerClassifier, self).__init__()
        self.embedding = nn.Linear(input_dim, hidden_dim)
        self.transformer = nn.TransformerEncoder(nn.TransformerEncoderLayer(d_model=hidden_dim, nhead=num_heads), num_layers)
        self.fc = nn.Linear(hidden_dim, num_classes)

    def forward(self, x):
        embedded = self.embedding(x)
        embedded = embedded.unsqueeze(1)
        embedded = embedded.permute(1,0,2)  # 调整维度顺序
        output = self.transformer(embedded)
        mean_pooling = output.mean(dim=0)  # 均值池化
        logits = self.fc(mean_pooling)
        return logits


cnn_model = CNNFeatureExtractor()
transformer_model = TransformerClassifier(input_dim, hidden_dim, num_classes, num_layers, num_heads)

# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(transformer_model.parameters(), lr=0.001)


#device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
device = torch.device("cpu")
cnn_model.to(device)
transformer_model.to(device)

'''
for epoch in range(num_epochs):
    transformer_model.train()
    total_loss = 0
    sum = 0

    for batch_data, batch_labels in zip(a[0:train_num],b[0:train_num]):
        batch_data = torch.Tensor(batch_data).type(torch.float32)
        batch_data = batch_data.unsqueeze(1)
        batch_labels = torch.Tensor(batch_labels).type(torch.long)
        
        # 使用CNN提取特征
        features = cnn_model(batch_data)
        features = features.view(features.size(0), -1)  # 展平特征

        # 不使用CNN提取特征
        # features = batch_data.view(64,784)

        optimizer.zero_grad()
        logits = transformer_model(features)
        loss = criterion(logits, batch_labels)
        total_loss += loss.item()

        loss.backward()
        optimizer.step()

    average_loss = total_loss / train_num
    # average_loss = total_loss / len(train_loader)
    print(f"Epoch {epoch + 1}/{num_epochs}, Average Loss: {average_loss:.4f}")


# 测试模型
transformer_model.eval()

# 保存权重
# 定义文件路径，用于保存模型权重
save_path = "64-10.pth"
# 将模型的权重保存到文件
torch.save(transformer_model.state_dict(), save_path)
'''
save_path = "64-10.pth"
#直接调用保存的模型（但是这个模型的参数得一样）
transformer_model.load_state_dict(torch.load(save_path))
transformer_model.eval()

predictions = []
true_labels = []

with torch.no_grad():
    # for batch_data, batch_labels in zip(a[train_num:test_num],b[train_num:test_num]):
    for batch_data, batch_labels in zip(csv_history,csv_labels):
        batch_data = torch.Tensor(batch_data).type(torch.float32)
        batch_data = batch_data.unsqueeze(1)
        batch_labels = torch.Tensor(batch_labels).type(torch.long)

        # 使用CNN提取特征
        features = cnn_model(batch_data)
        features = features.view(features.size(0), -1)  # 展平特征

        logits = transformer_model(features)

        predicted_labels = torch.argmax(logits, dim=1).cpu().numpy()
        print(predicted_labels)
        predictions.extend(predicted_labels)
        true_labels.extend(batch_labels.cpu().numpy())

accuracy = accuracy_score(true_labels, predictions)

num = len(predictions)
my_copy = my_copy[:num]

sum = 0
for i in range(0,num):
    if predictions[i] == my_copy[i]:
        sum += 1
print(sum / num)

import json

# 假设你有两个包含数据的列表
# 创建一个包含这两个列表的字典
data_dict = {'list1': [float(i) for i in my_copy[:400]], 'list2': [float(i) for i in predictions[:400]]}

# 指定要保存的JSON文件路径
json_file_path = "data.json"

# 使用json.dump()将数据字典保存到JSON文件
with open(json_file_path, 'w') as json_file:
    json.dump(data_dict, json_file)




print(f"Test Accuracy: {accuracy:.2f}")


