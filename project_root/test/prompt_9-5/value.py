import json
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import precision_recall_fscore_support, classification_report



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
            y1.append(int(round(float(labels))))
            y2.append(int(round(float(predict))))
    return y1, y2


def get_data(data_file,numbers=-1):
    list1,list2=file_name(data_file)
    list1 = list1[:numbers]
    list2 = list2[:numbers]
    return list1,list2


def get_result(data_file,numbers=-1):
    # 真实标签和预测标签的示例数据
    # true_labels = [1, 2, 2, 3, 1, 2, 2, 1, 3, 2]
    # predicted_labels = [1, 2, 2, 3, 1, 2, 2, 1, 3, 2]
    true_labels,predicted_labels = get_data(data_file,numbers)
    print(true_labels)
    print(predicted_labels)

    # 计算准确率
    accuracy = accuracy_score(true_labels, predicted_labels)
    print("准确率:", round(accuracy,4))

    # 计算宏平均精确度、召回率和F1分数
    macro_precision = precision_score(true_labels, predicted_labels, average='macro')
    macro_recall = recall_score(true_labels, predicted_labels, average='macro')
    macro_f1 = f1_score(true_labels, predicted_labels, average='macro')
    print("宏平均精确度:", round(macro_precision,4))
    print("宏平均召回率:", round(macro_recall,4))
    print("宏平均F1分数:", round(macro_f1,4))

    # 计算微平均精确度、召回率和F1分数
    micro_precision, micro_recall, micro_f1, _ = precision_recall_fscore_support(true_labels, predicted_labels, average='micro')
    print("微平均精确度:", round(micro_precision,4))
    print("微平均召回率:", round(micro_recall,4))
    print("微平均F1分数:", round(micro_f1,4))

    # 生成分类报告
    # report = classification_report(true_labels, predicted_labels)
    # print("分类报告:\n", report)
    value = round(accuracy,4)
    return value


numbers = 40
file_nums = ["01","02","03","04","05","06"]

file_num = "01"

file_stock = "data/stock-much/0000"
Linear="_16_4_DLinear_custom_ftM_sl16_ll4_pl4_dm512_nh8_el2_dl1_df2048_fc1_ebtimeF_dtTrue_Exp_0/output.txt"
AutoFormer="_ili_36_4_Autoformer_custom_ftM_sl16_ll4_pl4_dm512_nh8_el2_dl1_df2048_fc3_ebtimeF_dtTrue_Exp_0/output.txt"
Informer="_ili_36_4_Informer_custom_ftM_sl16_ll4_pl4_dm512_nh8_el2_dl1_df2048_fc3_ebtimeF_dtTrue_Exp_0/output.txt"
Transformer="_ili_36_4_Transformer_custom_ftM_sl16_ll4_pl4_dm512_nh8_el2_dl1_df2048_fc3_ebtimeF_dtTrue_Exp_0/output.txt"
models=[Linear,AutoFormer,Informer,Transformer]

result_accs = []
def result(file_nums):
    for file_num in file_nums:
        files=[]
        input_file = "data/" + file_num+".txt"
        files.append(input_file)
        for model in models:
            name = file_stock + file_num + model
            files.append(name)
        print(files)
        result_acc = []
        for File in files:
            value = get_result(File)
            result_acc.append(value)
        result_accs.append(result_acc)

result(file_nums)

print(result_accs)
