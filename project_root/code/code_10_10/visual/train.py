from gensim.models import Word2Vec
import matplotlib.pyplot as plt
import itertools
import data_utils
import glob

number = 4

"""
#传入数据
file_pattern = "filter_data/*.csv"
all_file = []
for file_name in glob.glob(file_pattern):
    print(file_name)
    all_file.append(file_name)
sentences,_ = data_utils.get_datas(all_file)


#添加初始集合
characters = 'ABCDEFGHIJKL'
permutations_1 = list(itertools.permutations(characters, 1))
permutations_2 = list(itertools.permutations(characters, 2))
total = permutations_1 + permutations_2
data = []
for p in total:
    data.append(''.join(p))

sentences.append(data)


# 构建Word2Vec模型
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, sg=0)

# 训练模型
model.train(sentences, total_examples=len(sentences), epochs=10)

#保存模型
model.save("one_model")
"""

#加载模型
model = Word2Vec.load("two_model")
# print(model.wv.vectors)
# print(model.wv.vectors.shape)
# input()


# 选择一组词汇进行可视化
characters = 'ABCDEFGHIJKL'
permutations_1 = list(itertools.permutations(characters, 1))
permutations_2 = list(itertools.permutations(characters, 2))
#total = permutations_1 + permutations_2
total =  permutations_2
data = []
for p in total:
    data.append(''.join(p))
temp = []
s = ['A','B','C','D']
for i in data:
    if i[0] in s and i[-1] in s:
        temp.append(i)
selected_words = temp
#selected_words = ["A", "B", "C", "D", "E", "F","G","H","I","J","K","L"]
#temp = ["B", "C", "D", "E", "F","G","H","I","J","K","L"]
# selected_words = [ 'A'+str(i) for i in temp]

# 获取选定词汇的词向量
word_vectors = [model.wv[word] for word in selected_words]

# 使用PCA进行降维到2维空间
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
word_vectors_2d = pca.fit_transform(word_vectors)

# 创建散点图来可视化词向量
plt.figure(figsize=(10, 8))
for i in range(len(selected_words)):
    plt.scatter(word_vectors_2d[i, 0], word_vectors_2d[i, 1], label=selected_words[i])
    plt.annotate(selected_words[i], (word_vectors_2d[i, 0], word_vectors_2d[i, 1]))
plt.legend()
plt.title("Word2Vec Visualization")
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
file_name = str(number)+".png"
plt.savefig(file_name)
