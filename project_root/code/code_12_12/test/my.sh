#!/bin/bash

# 源文件夹路径
source_folder="./test3_no_error"

# 目标文件夹路径
target_folder="./val"

# 切换到源文件夹

cd "$source_folder" || exit
mkdir val

# 使用ls列出所有文件，shuf随机排序，head选择前30个文件，然后将它们复制到目标文件夹
ls | shuf -n 200 | xargs -I {} mv "{}" "$target_folder"

mkdir train 

mv *.txt train
