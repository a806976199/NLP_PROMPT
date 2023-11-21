import os
import glob
all_file = glob.glob('train/*.txt')
all_file = sorted(all_file)
# file_list = [int(i[8:-4]) for i in all_file]
# file_name_list=[]
for i in range(0,len(all_file)):
    if i >= 10000:
         os.remove(all_file[i])  # 删除文件的操作，请小心使用，确保你需要删除的文件已经备



all_file = glob.glob('val/*.txt')
all_file = sorted(all_file)
# file_list = [int(i[6:-4]) for i in all_file]
# file_name_list=[]
for i in range(0,len(all_file)):
    if i >= 20:
         os.remove(all_file[i])  # 删除文件的操作，请小心使用，确保你需要删除的文件已经备
