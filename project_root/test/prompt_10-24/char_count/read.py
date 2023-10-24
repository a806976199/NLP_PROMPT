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
#新加入都数据
with open('transformer_lstm.json','r') as file:
    json_data = json.load(file)
transformer_lstm = json_data

with open('transformer_lstm_zero.json','r') as file:
    json_data = json.load(file)
transformer_lstm_zero = json_data

with open('transformer_model.json','r') as file:
    json_data = json.load(file)
transformer_model = json_data

with open('transformer_zero.json','r') as file:
    json_data = json.load(file)
transformer_zero = json_data

with open('lstm_attention_zero.json','r') as file:
    json_data = json.load(file)
lstm_attention_zero = json_data

with open('lstm_attention.json','r') as file:
    json_data = json.load(file)
lstm_attention = json_data


print(sum(chatglm_25['correct']) / len(chatglm_25['correct']))

res = dict()
res['name'] = chatglm_25['name'][:700]
res['chatglm_25'] = chatglm_25['correct'][:700]
res['zero_one'] = zero_one_25['correct'][:700]
res['initial_25'] = initial_25['correct'][:700]
res['word2vec_25'] = word2vec_25['correct'][:700]
res['word2vec_100'] = word2vec_100['correct'][:700]

#新加入都数据
res['lstm_attention'] = lstm_attention['correct'][:700]
res['transformer_lstm'] = transformer_lstm['correct'][:700]
res['transformer_lstm_zero'] = transformer_lstm_zero['correct'][:700]
res['transformer_model'] = transformer_model['correct'][:700]
res['transformer_zero '] = transformer_zero['correct'][:700]
res['lstm_attention_zero'] = lstm_attention_zero['correct'][:700]






df = pd.DataFrame(res)
df.to_excel('result.xlsx',index=False)
