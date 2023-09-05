import json
import math
import matplotlib.pyplot as plt
import openpyxl
import torch
import torch.nn.functional as F

# 打开包含 JSON 对象的文件
# 10000-8-4-one.txt
# 20000-mix-one.txt
# 30000-16-8-much.txt
# 30000-16-8-one.txt
# 30000-8-4-much.txt

#file_list=['chatglm2_zero_test_new-prompt.txt','mix_1000_8-18-2_4-function.txt','mix_5000_8-18-2_4-function.txt','model_test_new-prompt.txt']

file_list=['data/tan-initial.txt','data/tan-result.txt','data/linear-initial.txt','data/linear-result.txt','data/after_decode.txt','data/no_revin.txt']
#file_list=['mix_1000_8-18-2_4-function.txt']

def get_png(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()

    # 解析每个 JSON 对象并提取数据
    extracted_data = []
    for line in data:
        json_data = json.loads(line)
        # labels = list(map(float, json_data["labels"].split(",")))
        # predict = list(map(float, json_data["predict"].split(",")))
        # json_data["labels"]=json_data["labels"][8:]
        # json_data["predict"]=json_data["predict"][8:]
        # print(json_data["labels"])
        json_data["labels"]=json_data["labels"][:]
        json_data["predict"]=json_data["predict"][:]
        labels = [float(x) if x.replace(".", "", 1).isdigit() else 0 for x in json_data["labels"].split(",")]
        predict = [float(x) if x.replace(".", "", 1).isdigit() else 0 for x in json_data["predict"].split(",")]
        extracted_data.append({"labels": labels, "predict": predict})



    items_to_remove = []
    # 得到必要的信息
    for item in extracted_data:
        # print("Labels:", item["labels"])
        # print("Predict:", item["predict"])
        if len(item["labels"]) != len(item["predict"]):
            items_to_remove.append(item)

    #删除的不对等的元素
    for item in items_to_remove:
        extracted_data.remove(item)


    #元素对比长度对等的元素的比例
    error_length = len(items_to_remove)
    normal_length = len(extracted_data)
    correct_rate = normal_length / (normal_length + error_length)

    #计算MSE,MAE
    n = len(extracted_data)  # 字典数据的总数
    mae_sum = 0.0
    mse_sum = 0.0

    #计算每一步的SE（平方误差）和AE（平均误差）
    #2范数
    res_se=[]
    #1范数
    res_ae=[]

    for item in extracted_data:
        labels = item["labels"]
        labels = torch.tensor(labels).float()
        mean = torch.mean(labels)
        std = torch.std(labels)
        if std == 0:
            std = 1e-8
        labels = (labels - mean) / std
        predict = item["predict"]
        predict = torch.tensor(predict).float()
        mean = torch.mean(predict)
        std = torch.std(predict)
        if std == 0:
            std = 1e-8
        predict = (predict - mean) / std
        # mse
        res_se.append(torch.mean(torch.abs(labels - predict)))
        # mae
        res_ae.append(torch.mean((labels - predict)**2))

    # 如果误差大于50,直接不要这个元素了    # 得到必要的信息
    # mylist = []
    # for i in range(len(res_se)):
    #     if (res_se[i] < 10) and (res_ae[i] < 10):
    #         mylist.append(i)
    # aa = [res_se[i] for i in mylist]
    # bb = [res_ae[i] for i in mylist]
    # res_se = aa
    # res_ae = bb
    # print(aa)
    # result_number = len(mylist)
    # result_number = 200

    # 计算平均绝对误差 (MAE),计算均方误差 (MSE)
    mae = torch.mean(torch.tensor(res_ae).float())
    mse = torch.mean(torch.tensor(res_se).float())
    print(file_path[:-4])
    print("correct_rate:",correct_rate)
    print("MAE:", mae)
    print("MSE:", mse)
    print((len(res_se)))
    # 获得给定的数据
    a1,a2 = res_ae,res_se 
    label_a='-'+ file_path[:-4]


    # 绘制单个表里面的多个图
    fig, axes = plt.subplots(1, 2, figsize=(6, 8))

    # 根据需要绘制子图
    # axes[0, 0].plot(range(len(a1)), a1,label='1-norm')
    # axes[0, 0].plot(range(len(a1)), [mae]*len(a1),label='mae')
    # axes[0, 0].set_xlabel('The number of prediction')
    # axes[0, 0].set_ylabel('Error')
    # axes[0, 0].set_title('MAE'+label_a)  # 设置图表标题

    # axes[1, 0].plot(range(len(a2)), a2)
    # axes[1, 0].plot(range(len(a2)), [mse]*len(a2),label='mse')
    # axes[1, 0].set_xlabel('The number of prediction')
    # axes[1, 0].set_ylabel('Error')
    # axes[1, 0].set_title('MSE'+label_a)  # 设置图表标题

    axes[0].plot(range(len(a1)), a1,label='Absolute Error')
    axes[0].plot(range(len(a1)), [mae]*len(a1),label='mae:'+"{:.4f}".format(mae))
    #axes[0].set_xlabel('The number of prediction,'+'rate:'+"{:.4f}".format(correct_rate))
    axes[0].set_xlabel('The number of prediction')
    axes[0].set_ylabel('Error')
    axes[0].set_title('MAE'+label_a)  # 设置图表标题
    axes[0].legend()

    axes[1].plot(range(len(a2)), a2,label='Squared Error')
    axes[1].plot(range(len(a2)), [mse]*len(a2),label='mse:'+"{:.4f}".format(mse))
    #axes[1].set_xlabel('The number of prediction,'+'rate:'+"{:.4f}".format(correct_rate))
    axes[1].set_xlabel('The number of prediction')
    axes[1].set_ylabel('Error')
    axes[1].set_title('MSE'+label_a)  # 设置图表标题
    axes[1].legend()

    # 调整子图之间的间距
    plt.tight_layout()

    # 保存图片
    plt.savefig(file_path[:-4]+'.png')

    # 显示图表
    #plt.show()

    return file_path[:-4],mae,mse,correct_rate


data=[]
data.append(["NAME","MAE","MSE","RATE"])
for item in file_list:
    data.append(get_png(item))



'''
# 创建一个新的Excel工作簿
workbook = openpyxl.Workbook()

# 获取默认的活动工作表
sheet = workbook.active

# 将数据写入工作表
for row in data:
    sheet.append(row)

# 保存Excel文件
workbook.save('data.xlsx')

import torch
import torch.nn.functional as F

# 假设已经有了归一化后的预测值和真实值张量
normalized_predictions = torch.tensor([0.25, 0.35, 0.42, 0.51])
normalized_targets = torch.tensor([0.20, 0.28, 0.39, 0.50])

# 计算归一化后的MAE（Mean Absolute Error）
normalized_mae = torch.mean(torch.abs(normalized_predictions - normalized_targets))
print("Normalized MAE:", normalized_mae.item())

# 计算归一化后的MSE（Mean Squared Error）
normalized_mse = torch.mean((normalized_predictions - normalized_targets)**2)
print("Normalized MSE:", normalized_mse.item())


    # 如果误差大于50,直接不要这个元素了    # 得到必要的信息
    mylist = []
    for i in range(len(res_se)):
        if (res_se[i] < 10) and (res_ae[i] < 10):
            mylist.append(i)
    aa = [res_se[i] for i in mylist]
    bb = [res_ae[i] for i in mylist]
    res_se = aa
    res_ae = bb
    print(aa)
    result_number = len(mylist)
    #计算平均误差
    for i in range(result_number):
        # 累加绝对误差
        mae_sum += res_ae[i]
        # 累加绝对误差的平方
        mse_sum += res_se[i] * res_se[i]


    # 计算平均绝对误差 (MAE),计算均方误差 (MSE)
    mae = mae_sum / result_number
    mse = mse_sum / result_number
    print(file_path[:-4])
    correct_rate = len(mylist) / (normal_length + error_length)
    print("correct_rate:",correct_rate)
    print("MAE:", mae)
    print("MSE:", mse)
    print((len(res_se)))
    # 获得给定的数据
    a1,a2 = res_ae,res_se 
    label_a='-'+ file_path[:-4]


'''
