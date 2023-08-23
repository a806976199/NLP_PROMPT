import json
import glob


# 定义要合并的多个 JSON 文件的文件名模式
file_pattern = 'test*/dev.json'

# 创建一个空的列表，用于存储所有 JSON 数据
merged_data = []

# 逐个读取并合并 JSON 文件
sum = 0
for file_name in glob.glob(file_pattern):
    sum += 1
for j in range(sum):
    file_name = "test" + str(j) + "/dev.json"
    print(file_name)
    with open(file_name, 'r') as file:
        json_data = json.load(file)
        for i in range(0,100,20):
            merged_data.append(json_data[i])

# 将合并后的 JSON 数据写入新的文件
output_file = 'dev_small.json'
with open(output_file, 'w') as file:
    json.dump(merged_data, file, indent=4)

print("合并完成，结果保存在", output_file)

