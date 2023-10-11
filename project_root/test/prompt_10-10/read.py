import json
import pandas as pd
from openpyxl import Workbook 

with open('initial_25.json','r') as file:
    json_data = json.load(file)
initial_25 = json_data

with open('word2vec_25.json','r') as file:
    json_data = json.load(file)
word2vec_25 = json_data

with open('word2vec_100.json','r') as file:
    json_data = json.load(file)
word2vec_100 = json_data

with open('zero_one.json','r') as file:
    json_data = json.load(file)
zero_one_25 = json_data

with open('chatglm_25.json','r') as file:
    json_data = json.load(file)
chatglm_25 = json_data

print(sum(chatglm_25['correct']) / len(chatglm_25['correct']))

res = dict()
res['name'] = chatglm_25['name'][:600]
res['chatglm_25'] = chatglm_25['correct'][:600]
res['zero_one'] = zero_one_25['correct'][:600]
res['initial_25'] = initial_25['correct'][:600]
res['word2vec_25'] = word2vec_25['correct'][:600]
res['word2vec_100'] = word2vec_100['correct'][:600]

df = pd.DataFrame(res)
df.to_excel('res.xlsx',index=False)
