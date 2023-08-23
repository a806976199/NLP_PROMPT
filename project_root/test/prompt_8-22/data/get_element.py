import json

# 打开JSON文件并加载数据
file_name1 = "3-element.json"
with open(file_name1, 'r') as file:
    data = json.load(file)

# 遍历每个数据项并提取内容和摘要
my_list = []
for item in data:
    summary = item['summary']
    my_list.append(summary)

# 打开文本文件并逐行读取数据
file_name2 = "result.txt"
with open(file_name2, 'r') as file:
    lines = file.readlines()


# 遍历每一行数据并提取标签和预测值
# predicts = []
# for line in lines:
#     # 使用逗号拆分行数据
#     data = line.strip().split(',')
#     predict = [float(value) for value in data[1].split()]
#     predicts.append(predict)
#     print("Predict:", predict)
# 遍历每一行数据并提取"labels"和"predict"的内容
predicts = []
labels = []
for line in lines:
    # 解析JSON格式的数据
    data = json.loads(line)
    predict = data["predict"]

    cleaned_data = predict.replace(' ', '').split(',')
    data_list = [float(value) for value in cleaned_data]
    predicts.append(data_list)
    
    label = data["labels"]
    cleaned_data = label.replace(' ', '').split(',')
    data_list = [float(value) for value in cleaned_data]
    labels.append(data_list)

print(my_list[1])
print(predicts[0])
print(labels[0])

from RevIN import RevIN

import torch 

print("start")

print(my_list[1])

x = torch.tensor(my_list[0]).T

print(x)

layer = RevIN(x.shape[1])

x_revin = layer(x,mode='norm')


y_revin = layer(x_revin,mode='denorm')

print(x_revin)
print(y_revin)

"""
input: 三元组[i]，labels[i],predicts[i]
output:f(labels[i]),f(predicts[i])
"""
print("-------------------")
print(my_list[0])
print(predicts[0])
print(labels[0])


x = labels[0]
y = predicts[0]
z = my_list[0]


def transform(a:list,b:list,c:list):
    a = torch.tensor(a)
    b = torch.tensor(b)
    c = torch.tensor(c).T
    result_a = []
    result_b = []
    layer = RevIN(c.shape[1])
    c_revin = layer(c,mode='norm')
    for i in range(a.shape[0]):
        res = layer(a[0],mode='denorm')[0]
        result_a.append(res.tolist()[-1])
    for i in range(b.shape[0]):
        res = layer(b[0],mode='denorm')[0]
        result_b.append(res.tolist()[-1])
    return result_a,result_b

aa,bb = transform(x,y,z)
print("aa")
print(aa)
print("bb")
print(bb)

res_x = []
res_y = []
for i in range(200):
    res1,res2 = transform(labels[i],predicts[i],my_list[i])
    res_x.append(res1)
    res_y.append(res2)

# # 要保存的数据
# labels_list = res_x[i]
# predict_list = res_y[i]

# # 将列表中的元素转换为逗号分隔的字符串
# labels_str = ', '.join(map(str, labels_list))
# predict_str = ', '.join(map(str, predict_list))

# # 构建字典并格式化为字符串
# data_dict = {
#     "labels": labels_str,
#     "predict": predict_str
# }
# formatted_data = f'{{"labels": "{labels_str}", "predict": "{predict_str}"}}'

# # 保存格式化的字符串到txt文件
# with open('output.txt', 'w') as file:
#     file.write(formatted_data)

"""
input:两种数据集
output:保存到文件
"""
def output(x,y):
    for i in range(len(res_x)):
        # 将列表中的元素转换为逗号分隔的字符串
#        labels_str = ', '.join(map(str, x[i]))
        labels_str = my_list[i][1]
        predict_str = ', '.join(map(str, y[i]))

        # 构建字典并格式化为字符串
        data_dict = {
            "labels": labels_str,
            "predict": predict_str
        }
        formatted_data = f'{{"labels": "{labels_str}", "predict": "{predict_str}"}}'

        # 保存格式化的字符串到txt文件
        with open('output.txt', 'a') as file:
            file.write(formatted_data + '\n')
        
print("res_x",res_x[0])
print("res_y",res_y[0])
output(res_x,res_y)
