import json
import re
import glob



def get_content(s):
    # 使用正则表达式提取内容
    pattern = re.compile(r'IN: (.+) OUT: (.+)')
    matches = pattern.findall(s)

    # 分别提取IN和OUT后面的内容
    if matches:
        # 分别提取IN和OUT后面的内容
        in_values = [match[0] for match in matches]
        out_values = [match[1] for match in matches]
    else:
        print("No match found.")

    # 我的字典格式内容
    my_dict= dict()
    my_dict['content'] = in_values[0]
    my_dict['summary'] = out_values[0]
    return my_dict

def get_data(file_names,judge=True):
    #从txt文本中获得文本数据
    data=[]

    #最终结果
    result=[]
    for file_name in file_names:
        with open(file_name,'r') as file:
            data_result=file.readlines()
            for i in range(1,15):
                data.append(data_result[i][:-1])
    for element in data:
        result.append(get_content(element)) 
     
    # 将字典保存到文件
    if judge == True:
        file = 'train.json'
    else:
        file = 'dev.json'
    with open(file, 'w') as json_file:
        json.dump(result, json_file,indent=2)

file_list = glob.glob('*.txt')
file_list = sorted(file_list)
print(file_list)
get_data(file_list)
