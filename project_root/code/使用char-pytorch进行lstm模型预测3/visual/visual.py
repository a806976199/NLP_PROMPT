from gensim.models import Word2Vec
import matplotlib.pyplot as plt

import data_utils

#传入数据
file = "../filter_data/AGR.csv"

sentences,_ = data_utils.get_data(file)
sentences.append(["A", "B", "C", "D", "E", "F","G","H","I","J","K","L"])

# 构建Word2Vec模型
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, sg=0)

# 训练模型
model.train(sentences, total_examples=len(sentences), epochs=10)

#保存模型
#model.save(“name”)

#加载合并数据集下的模型
#model = Word2Vec.load("total_model")

# 选择一组词汇进行可视化
selected_words = ["A", "B", "C", "D", "E", "F","G","H","I","J","K","L"]

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

plt.savefig("result.png")
