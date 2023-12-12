import random

"""
总函数
input:输入4个数字而已1,...,9

output:输出 一个文件

小函数:
input:数字

output:输出一串字符

"""
def num_one(x,y=True):
    a = ''
    s = ''
    if y:
        a = ' 1'
    else:
        a = ' -1'
    for i in range(0,x):
        s += a
    return s

def num_ten(x,y=True):
    a = ''
    s = ''
    if y:
        a = ' 10'
    else:
        a = ' -10'
    for i in range(0,x):
        s += a
    return s

def sum(x):
    s = "IN: sum "
    s += str(x) + " OUT:"
    s += num_one(x)
    return s

def sub(x):
    s = "IN: sub "
    s += str(x) + " OUT:"
    s += num_one(x,False)
    return s

def sum_sub(a,b):
    s = 'IN: sum ' + str(a) +' sub '+str(b) +' OUT:'
    x = num_one(a)
    y = num_one(b,False)
    return s + x + y

def sub_sum(a,b):    
    s = 'IN: sub ' + str(a) +' sum '+str(b) +' OUT:'
    x = num_one(a,False)
    y = num_one(b)
    return s + x + y

def prod(a,b):
    s = 'IN: '+str(a)+' prod '+str(b)+' OUT:'
    for i in range(0,b):
        s += ' '+str(a)
    return s

def sum_sub_sub(a,b,c):
    s = 'IN: sum '+str(a)+' sub '+str(b)+' sub '+str(c)+' OUT:'
    s += num_one(a)
    s += num_one(b,False)
    s += num_one(c,False)
    return s
def sum_sub_sum(a,b,c):
    s = 'IN: sum '+str(a)+' sub '+str(b)+' sum '+str(c)+' OUT:'
    s += num_one(a)
    s += num_one(b,False)
    s += num_one(c)
    return s

def prod_sum(a,b,c):
    s = 'IN: '+str(a)+' prod '+str(b)+' sum '+str(c)+' OUT:'
    for i in range(0,b):
        s += ' '+str(a)
    s += num_one(c)
    return s

def prod_sub(a,b,c):
    s = 'IN: '+str(a)+' prod '+str(b)+' sub '+str(c)+' OUT:'
    for i in range(0,b):
        s += ' '+str(a)
    s += num_one(c,False)
    return s
    
def prod_sum_sum(a,b,c,d):
    s = prod_sum(a,b,c) + num_one(d)
    return s
    
def prod_sub_sum(a,b,c,d):
    s = prod_sub(a,b,c) + num_one(d)
    return s

def prod_sum_sub(a,b,c,d):
    s = prod_sum(a,b,c) + num_one(d,False)
    return s
    
def sum_prod(a,b):
    s = 'IN: ' + 'sum ' + str(a)+' prod ' + str(b) +' OUT:'
    for i in range(0,b):
        s += num_one(a)
    return s

def sub_prod(a,b):
    s = 'IN: ' + 'sub ' + str(a)+' prod ' + str(b) +' OUT:'
    for i in range(0,b):
        s += num_one(a,False)
    return s

def num_kuo(x):
    s = ''
    for i in range(0,x):
        s += str(' [u1]')
    return s

def grammar(a,b,c,d,e):
    result = []

    s1 = str(a) + ' -> ' + str(a)
    s2 = str(b) + ' -> ' + str(b)
    s3 = str(c) + ' -> ' + str(c)
    s4 = str(d) + ' -> ' + str(d)
    s5 = str(e) + ' -> ' + str(e)
    
    s6 = 'u1 '+str(a)+' ->' + num_kuo(a)
    s7 = 'u1 '+str(b)+' ->' + num_kuo(b)
    s8 = 'u1 '+str(c)+' ->' + num_kuo(c)
    s9 = 'u1 '+str(d)+' ->' + num_kuo(d)
    s10 = 'u1 '+str(e)+' ->' + num_kuo(e)
    
    # s9 = 'u1 prod ' +str(a)+' ->' + num_kuo(a)
    # s10 = 'u1 prod ' +str(b)+' ->' + num_kuo(b)
    # s11 = 'u1 prod ' +str(c)+' ->' + num_kuo(c)
    # s12 = 'u1 prod ' +str(d)+' ->' + num_kuo(d)

    result.append('sum -> 1')
    result.append('sub -> -1')
    result.append('pos -> 10')
    result.append('pas -> -10')
    result.append(s1)
    result.append(s2)
    result.append(s3)
    result.append(s4)
    result.append(s5)
    result.append(s6)
    result.append(s7)
    result.append(s8)
    result.append(s9)
    result.append(s10)
    # result.append(s11)
    # result.append(s12)
    for i in result:
        print(i)
    return result
'''
# Generate random numbers for data
def generate_random_numbers(n):
    return ' '.join([str(random.randint(1, 10)) for _ in range(n)])

# Randomly generate some data
for data_list in [support_data, query_data]:
    for i in range(len(data_list)):
        data_list[i] = f"{data_list[i]} {generate_random_numbers(random.randint(1, 5))}"

# Print the generated data
print("*SUPPORT*")
for item in support_data:
    print(f"IN: {item}")

print("\n*QUERY*")
for item in query_data:
    print(f"IN: {item}")

print("\n*GRAMMAR*")
for item in grammar_data:
    print(item)
'''

def result(a,b,c,d):
    print("*SUPPORT*")
    print(sum(b))
    print(sub(c))
    print(sum_sub(a,d))
    print(sub_sum(d,a))
    print(prod(b,a))
    print(sum_sub_sub(c,d,b))
    print(sum_sub_sum(a,b,b))
    print(prod_sum(a,b,c))
    print(prod_sub(d,c,a))
    print(prod_sum_sum(a,b,a,b))
    print(prod_sub_sum(c,a,d,b))
    print(prod_sum_sub(c,b,d,a))
    print(sum_prod(a,d))
    print(sub_prod(b,c))
    print()
    print('*QUERY*')
    print(sum(a))
    print(sub(d))
    print(sum_sub(b,c))
    print(sub_sum(c,b))
    print(prod(c,d))
    print(sum_sub_sum(d,c,a))
    print(prod_sum(c,b,d))
    print(prod_sub(d,a,c))
    print(sum_prod(d,c))
    print(sub_prod(a,b))
    print()
    print('*GRAMMAR*')
    grammar(a,b,c,d)

def result2(a,b,c,d):
    print("*SUPPORT*")
    print(prod(c,b))
    print(prod(a,d))
    print(sub_prod(b,d))
    print(sum_prod(a,c))
    print(sum_sub_sum(b,a,c))
    print(sum_sub(b,c))
    print(sub_sum(c,b))
    print(prod(c,d))
    print(sum_sub_sum(d,c,a))
    print(prod_sum(c,b,d))
    print(prod_sub(d,a,c))
    print(sum_sub_sub(c,d,b))
    print(prod_sum(a,d,c))
    print(prod_sub(c,d,a))
    print()
    print('*QUERY*')
    my_query_list = []
    my_query_list.append(sub_sum(c,b))
    my_query_list.append(sum_sub_sum(d,c,a))
    my_query_list.append(prod_sum(c,b,d))
    my_query_list.append(prod_sub(d,a,c))
    my_query_list.append(sum_prod(d,c))
    my_query_list.append(sub_sum(d,a))
    my_query_list.append(prod(b,a))
    my_query_list.append(sum_sub_sub(c,d,b))
    my_query_list.append(prod_sub(d,c,a))
    my_query_list.append(sum_prod(a,d))
    my_query_list.append(sub_sum(a,d))
    my_query_list.append(sum_sub_sum(b,c,d))
    my_query_list.append(prod_sum(c,a,b))
    my_query_list.append(prod_sub(b,a,d))
    my_query_list.append(sum_prod(c,a))
    my_query_list.append(sub_sum(c,b))
    my_query_list.append(prod(c,a))
    my_query_list.append(sum_sub_sub(c,a,d))
    my_query_list.append(prod_sub(b,c,d))
    my_query_list.append(sum_prod(a,c))
    for num in range(0,10):
        choice = random.choice([0, 10]) + num
        # print(choice)
        print(my_query_list[choice])
        # print(my_query_list[num])
        
    print()
    print('*GRAMMAR*')
    grammar(a,b,c,d)


def pas_sum(a,b,c):    
    s = 'IN: pas ' + str(a) +' sub '+str(b) + ' sum ' + str(c) + ' OUT:'
    x = num_ten(a,False)
    y = num_one(b,False)
    z = num_one(c)
    return s + x + y + z

def pos_sub(a,b,c):    
    s = 'IN: pos ' + str(a) +' sum '+str(b) + ' sub ' + str(c) + ' OUT:'
    x = num_ten(a)
    y = num_one(b)
    z = num_one(c,False)
    return s + x + y + z

def sub_pos(a,b,c):    
    s = 'IN: sub '+ str(a) + ' pos ' + str(b) +' sum '+ str(c) + ' OUT:'
    x = num_one(a,False)
    y = num_ten(b)
    z = num_one(c)
    return s + x + y + z

def sum_pos(a,b,c):    
    s = 'IN: sum '+ str(a) + ' pos ' + str(b) +' sum '+ str(c) + ' OUT:'
    x = num_one(a)
    y = num_ten(b)
    z = num_one(c)
    return s + x + y + z


def sum_pas(a,b,c):    
    s = 'IN: sum '+ str(a) + ' pas ' + str(b) +' sub '+ str(c) + ' OUT:'
    x = num_one(a)
    y = num_ten(b,False)
    z = num_one(c,False)
    return s + x + y + z

def pos_pas(a,b,c,d):    
    s = 'IN: pos ' +str(a)+ ' sum '+ str(b) + ' pas ' + str(c) +' sub '+ str(d) + ' OUT:'
    w = num_ten(a)
    x = num_one(b)
    y = num_ten(c,False)
    z = num_one(d,False)
    return s + w + x + y + z


def pas_pos(a,b,c,d):    
    s = 'IN: pas ' +str(a)+ ' sub '+ str(b) + ' pos ' + str(c) +' sum '+ str(d) + ' OUT:'
    w = num_ten(a,False)
    x = num_one(b,False)
    y = num_ten(c)
    z = num_one(d)
    return s + w + x + y + z

def sum_pas_sum(a,b,c,d):    
    s = 'IN: sum '+ str(a) + ' pas ' + str(b) +' sub '+ str(c) + ' sum '+str(d) + ' OUT:'
    x = num_one(a)
    y = num_ten(b,False)
    z = num_one(c,False)
    w =  num_one(d)
    return s + x + y + z + w

def pas_pos(a,b,c,d):    
    s = 'IN: pas ' +str(a)+ ' sub '+ str(b) + ' pos ' + str(c) +' sum '+ str(d) +' OUT:'
    w = num_ten(a,False)
    x = num_one(b,False)
    y = num_ten(c)
    z = num_one(d)
    return s + w + x + y + z 

def pas_pos_sum(a,b,c,d,e):    
    s = 'IN: pas ' +str(a)+ ' sub '+ str(b) + ' pos ' + str(c) +' sum '+ str(d) +' sum ' + str(e) + ' OUT:'
    w = num_ten(a,False)
    x = num_one(b,False)
    y = num_ten(c)
    z = num_one(d)
    v = num_one(e)
    return s + w + x + y + z  + v

def pas_sum_sub(a,b,c,d):    
    s = 'IN: pas ' + str(a) +' sub '+str(b) + ' sum ' + str(c) +' sub ' + str(d) + ' OUT:'
    x = num_ten(a,False)
    y = num_one(b)
    z = num_one(c)
    w = num_one(d,False)
    return s + x + y + z + w

def pos_sub_sum(a,b,c,d):    
    s = 'IN: pos ' + str(a) +' sum '+str(b) + ' sub ' + str(c) +' sum ' + str(d) + ' OUT:'
    x = num_ten(a)
    y = num_one(b)
    z = num_one(c,False)
    w = num_one(d)
    return s + x + y + z + w

def sum_sub_pos(a,b,c,d):    
    s = 'IN: sum ' +str(d) +' sub '+ str(a) + ' pos ' + str(b) +' sum '+ str(c) + ' OUT:'
    x = num_one(a,False)
    y = num_ten(b)
    z = num_one(c)
    w = num_one(d)
    return s +w+ x + y + z 

def sub_sum_pas(a,b,c,d):    
    s = 'IN: sub '+ str(d) + ' sum '+ str(a) + ' pas ' + str(b) +' sub '+ str(c) + ' OUT:'
    x = num_one(a)
    y = num_ten(b,False)
    z = num_one(c,False)
    w = num_one(d,False)
    return s +w+ x + y + z

def result3(a,b,c,d,e):
    print("*SUPPORT*")
    print(pas_sum(a,b,c))
    print(pos_sub(a,d,c))
    print(sub_pos(b,d,a))
    print(sum_pas(a,b,c))
    print(pos_pas(b,e,c,d))
    print(pas_pos(b,e,a,d))
    print(sub_sum(c,b))
    print(sum_pos(c,e,a))
    print(sum_pas_sum(d,b,c,a))
    print(pas_pos_sum(a,c,b,d,e))
    print(pas_sum_sub(b,d,a,c))
    print(pos_sub_sum(c,e,b,a))
    print(sum_sub_pos(a,d,e,b))
    print(sub_sum_pas(c,d,a,b))
    print()
    print('*QUERY*')
    my_query_list = []

    my_query_list.append(pas_sum(a,b,c))
    my_query_list.append(sub_pos(b,d,a))
    my_query_list.append(sum_pas(a,e,c))
    my_query_list.append(pos_pas(b,a,c,d))
    my_query_list.append(pas_pos(b,c,a,d))
    my_query_list.append(sum_pos(c,d,a))
    my_query_list.append(sum_pas_sum(d,b,c,a))
    my_query_list.append(pas_sum_sub(b,d,e,c))
    my_query_list.append(pos_sub_sum(c,e,b,a))
    my_query_list.append(sub_sum_pas(c,d,a,b))

    my_query_list.append(pas_sum(c,d,a))
    my_query_list.append(sub_pos(c,b,d))
    my_query_list.append(sum_pas(a,e,e))
    my_query_list.append(pos_pas(b,e,c,d))
    my_query_list.append(pas_pos(b,c,e,d))
    my_query_list.append(sum_pos(c,d,a))
    my_query_list.append(sum_pas_sum(d,e,c,a))
    my_query_list.append(pas_sum_sub(b,a,e,c))
    my_query_list.append(pos_sub_sum(c,e,d,a))
    my_query_list.append(sub_sum_pas(c,e,a,b))

    for num in range(0,10):
        choice = random.choice([0, 10]) + num
        # print(choice)
        print(my_query_list[choice])
        # print(my_query_list[num]);
        
    print()
    print('*GRAMMAR*')
    grammar(a,b,c,d,e)

from itertools import product

# 定义数字范围
digits = '123456789'

# 生成4位数的排列（包含重复数字）
product_4_digits = product(digits, repeat=5)

# 转换为整数并输出


import sys

# 打开一个文本文件，如果文件不存在会自动创建
# times的数据量
numbers = 16
i = 0
for element in product_4_digits:
    a = int(element[0])
    b = int(element[1])
    c = int(element[2])
    d = int(element[3])
    e = int(element[4])
    for j in range(0,numbers):
        file_name = str(i) + '.txt'
        with open(file_name, 'w') as file:
            # 重定向标准输出到文件
            sys.stdout = file
            # 这里写入你想要print的内容
            result3(a,b,c,d,e)
        
            sys.stdout = sys.__stdout__
        i += 1
        break;

