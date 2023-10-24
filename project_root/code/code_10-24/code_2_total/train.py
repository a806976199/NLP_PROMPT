#!/usr/bin/env python
# https://github.com/spro/char-rnn.pytorch

import torch
import torch.nn as nn
from torch.autograd import Variable
import argparse
import os
import csv 
import json
from tqdm import tqdm

from helpers import *
from model import *
from generate import *
import data_utils
import glob

# Parse command line arguments
argparser = argparse.ArgumentParser()
argparser.add_argument('filename', type=str)
argparser.add_argument('--model', type=str, default="lstm")
argparser.add_argument('--n_epochs', type=int, default=2000)
argparser.add_argument('--print_every', type=int, default=100)
argparser.add_argument('--hidden_size', type=int, default=100)
argparser.add_argument('--n_layers', type=int, default=4)
argparser.add_argument('--learning_rate', type=float, default=0.01)
argparser.add_argument('--chunk_len', type=int, default=12)
argparser.add_argument('--batch_size', type=int, default=20)
argparser.add_argument('--predict_length', type=int, default=2)
argparser.add_argument('--shuffle', action='store_true')
argparser.add_argument('--cuda', action='store_true')
args = argparser.parse_args()

if args.cuda:
    print("Using CUDA")

#获取相应的数据集(得到“26然后总的长度”)
import glob
file_pattern = "filter_data/*.csv"
all_file = []
for file_name in glob.glob(file_pattern):
    print(file_name)
    all_file.append(file_name)
all_file = sorted(all_file)[:-1]
file, file_len = data_utils.get_datas(all_file,args.chunk_len * 2,args.predict_length)

def random_training_set(chunk_len, batch_size):
    inp = torch.LongTensor(batch_size,chunk_len)
    target = torch.LongTensor(batch_size,chunk_len)
    for bi in range(batch_size):
        #主要输入字节转换
        index = random.randint(0, int(file_len * 0.8)- chunk_len)
        chunk = file[index]
        temp1 = char_tensor(chunk[:-1])
        temp2 = char_tensor(chunk[1:])
        inp[bi] = temp1
        target[bi] = temp2
        # inp[bi] = char_tensor(chunk[:-1])
        # target[bi] = char_tensor(chunk[1:])
    inp = Variable(inp)
    target = Variable(target)
    if args.cuda:
        inp = inp.cuda()
        target = target.cuda()
    return inp, target

def train(inp, target):
    hidden = decoder.init_hidden(args.batch_size)
    if args.cuda:
        # hidden = hidden.cuda()
        # 将元组中的每个张量移到GPU上
        hidden = (hidden[0].cuda(), hidden[1].cuda())
    decoder.zero_grad()
    loss = 0

    for c in range(args.chunk_len):
        output, hidden = decoder(inp[:,c], hidden)
        loss += criterion(output.view(args.batch_size, -1), target[:,c])

    loss.backward()
    decoder_optimizer.step()

    # return loss.data[0] / args.chunk_len
    return loss.item() / args.chunk_len

def save(save_file,data):
    # save_filename = os.path.splitext(os.path.basename(args.filename))[0] + '.pt'
    # torch.save(decoder, save_filename)
    # print('Saved as %s' % save_filename)
    with open(save_file,'w') as jsonfile:
        json.dump(data,jsonfile)
    print("数据已保存")
# Initialize models and start training

decoder = CharRNN(
    n_characters,
    args.hidden_size,
    n_characters,
    model=args.model,
    n_layers=args.n_layers,
)
decoder_optimizer = torch.optim.Adam(decoder.parameters(), lr=args.learning_rate)
criterion = nn.CrossEntropyLoss()

if args.cuda:
    decoder.cuda()
    
start = time.time()
all_losses = []
loss_avg = 0

try:
    #训练部分
    print("Training for %d epochs..." % args.n_epochs)
    for epoch in tqdm(range(1, args.n_epochs + 1)):
        loss = train(*random_training_set(args.chunk_len, args.batch_size))
        loss_avg += loss
        if epoch % args.print_every == 0:
            print('[%s (%d %d%%) %.4f]' % (time_since(start), epoch, epoch / args.n_epochs * 100, loss))
    #预测部分
    all_file = all_file[663:]
    for file in all_file:
        print(file,"is ok")
        filename = file
        file,file_len = data_utils.get_data(file,args.chunk_len,args.predict_length)
        predict_data = file[int(file_len * 0.8):]
        result={'predict':[],'labels':[]}
        sum = 0.0
        for my_str in predict_data:
            res = generate(decoder,prime_str = my_str[:-1],predict_len=1)
            result['predict'].append(data_utils.letter_to_number.get(res[-1][0]))
            result['labels'].append(data_utils.letter_to_number.get(my_str[-1][0]))
            if res[-1][0] == my_str[-1][0]:
                sum += 1.0
        print(round(sum/(file_len*0.2),4))
        save_file = 'save/'+filename[12:-4]+'.json'
        save(save_file,result)
        print("Saving...")
    
except KeyboardInterrupt:
    print("Saving before quit...")
    save()

