# import re

# data = {
#     "labels": "step0:-0.8898, 0.9453,step1:-0.8898, -0.0968, 0.7852, 0.9453,result:-0.8898, -0.0968, 0.7852, 0.9453",
#     "predict": "step0:-0.8938, 0.9454,step1:-0.8938, -0.0974, 0.7851, 0.9454,result:-0.8938, -0.0974, 0.7851, 0.9454"
# }

  


# # 使用正则表达式提取result和之间的内容
# result_pattern = r'result:(.*?)\,'
# result_match_labels = re.search(result_pattern, data["labels"])
# result_match_predict = re.search(result_pattern, data["predict"])

# if result_match_labels and result_match_predict:
#     result_labels = result_match_labels.group(1).strip()
#     result_predict = result_match_predict.group(1).strip()
#     print("Result in 'labels':", result_labels)
#     print("Result in 'predict':", result_predict)
# else:
#     print("Result not found in the given data.")


# import re

# data = {
#     "labels": "step0:-0.8898, 0.9453,step1:-0.8898, -0.0968, 0.7852, 0.9453,result:-0.8898, -0.0968, 0.7852, 0.9453",
#     "predict": "step0:-0.8938, 0.9454,step1:-0.8938, -0.0974, 0.7851, 0.9454,result:-0.8938, -0.0974, 0.7851, 0.9454"
# }

# # 使用正则表达式提取result和之间的内容
# result_pattern = r'result:(.*?)\,'

# def extract_result_with_quotes(input_string):
#     result_match = re.search(result_pattern, input_string)
#     if result_match:
#         result = result_match.group(1).strip()
#         # 将逗号替换为双引号
#         result_with_quotes = result.replace(",", "\",\"")
#         return f'"{result_with_quotes}"'
#     return None

# result_labels = extract_result_with_quotes(data["labels"])
# result_predict = extract_result_with_quotes(data["predict"])

# if result_labels and result_predict:
#     print("Result in 'labels':", result_labels)
#     print("Result in 'predict':", result_predict)
# else:
#     print("Result not found in the given data.")


#提取json文件的内容
import json 

res_label=[]
res_predict=[]

file_path = "zero2.txt"

with open(file_path, 'r') as file:
    data_dict = file.readlines()

for line in data_dict:
    json_data = json.loads(line)
    res_label.append(json_data["labels"])
    res_predict.append(json_data["predict"])



#寻在位置
import re


def find_result_position_with_regex(input_string):
    result_match = re.search(r'result', input_string)
    if result_match:
        return result_match.start()
    return None

# result_labels_position = find_result_position_with_regex(data["labels"])
# result_predict_position = find_result_position_with_regex(data["predict"])


# print(data["labels"][result_labels_position+8:])
# print(data["predict"][result_predict_position+8:])

labels = []
predicts = []

for label in res_label:
    result_labels_position = find_result_position_with_regex(label)
    if result_labels_position is not None:
        labels.append(label[result_labels_position+7:])

for predict in res_predict:
    result_predicts_position = find_result_position_with_regex(predict)
    if result_predicts_position is not None:
        predicts.append(predict[result_predicts_position+7:])

print(labels)
print(predicts)

#输出结果
output_path="output.txt"


# extract_data=[]
# for label,predict in labels,predicts:
#     extract_data.append({"labels":label,"predict":predict})


extract_data=[]
for label, predict in zip(labels, predicts):
    data_dict = {"labels": label, "predict": predict}
    extract_data.append(data_dict)


with open(output_path, 'w') as file:
    for item in extract_data:
        file.write(str(item) + '\n')
