import torch
import torch.nn as nn
import torchvision
from torchvision import transforms
import torch.optim as optim
from sklearn.metrics import accuracy_score
import random
import numpy as np 
# 准备数据集
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])


train_dataset = torchvision.datasets.MNIST(root='./data', train=True, transform=transform, download=True)
test_dataset = torchvision.datasets.MNIST(root='./data', train=False, transform=transform)

batch_size = 30

train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=batch_size)

# 定义CNN用于特征提取
class CNNFeatureExtractor(nn.Module):
    def __init__(self):
        super(CNNFeatureExtractor, self).__init__()
        self.cnn = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )

    def forward(self, x):
        return self.cnn(x)

# 定义Transformer模型
class TransformerClassifier(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_classes, num_layers, num_heads):
        super(TransformerClassifier, self).__init__()
        self.embedding = nn.Linear(input_dim, hidden_dim)
        self.transformer = nn.TransformerEncoder(nn.TransformerEncoderLayer(d_model=hidden_dim, nhead=num_heads), num_layers)
        self.fc = nn.Linear(hidden_dim, num_classes)

    def forward(self, x):
        embedded = self.embedding(x)
        embedded = embedded.unsqueeze(1)
        embedded = embedded.permute(1,0,2)  # 调整维度顺序
        output = self.transformer(embedded)
        mean_pooling = output.mean(dim=0)  # 均值池化
        logits = self.fc(mean_pooling)
        return logits

# 创建模型
input_dim = 64 * 1 * 1  # CNN的输出特征维度
#input_dim = 64 * 7 * 7  # CNN的输出特征维度
#input_dim = 16 * 7 * 7  # CNN的输出特征维度
hidden_dim = 256
num_classes = 10
num_layers = 2
num_heads = 4

cnn_model = CNNFeatureExtractor()
transformer_model = TransformerClassifier(input_dim, hidden_dim, num_classes, num_layers, num_heads)

# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(transformer_model.parameters(), lr=0.001)

# 训练模型
num_epochs = 1

#device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
device = torch.device("cpu")
cnn_model.to(device)
transformer_model.to(device)

for epoch in range(num_epochs):
    transformer_model.train()
    total_loss = 0
    sum = 0

    for batch_data, batch_labels in train_loader:
        batch_data, batch_labels = batch_data.to(device), batch_labels.to(device)
        batch_data = batch_data[:,:,12:16,12:16]
        # random_matrix = np.random.randint(-5, 6, size=(batch_size, 1, 4, 4))
        # data_type = torch.float32  # 例如，使用32位浮点数数据类型
        # batch_data = torch.Tensor(random_matrix).type(data_type)
        # batch_data = batch_data / 5

        # 使用CNN提取特征
        features = cnn_model(batch_data)
        features = features.view(features.size(0), -1)  # 展平特征

        # 不使用CNN提取特征
        # features = batch_data.view(64,784)

        optimizer.zero_grad()
        logits = transformer_model(features)
        loss = criterion(logits, batch_labels)
        total_loss += loss.item()

        loss.backward()
        optimizer.step()

    average_loss = total_loss / len(train_loader)
    print(len(train_loader))
    print(f"Epoch {epoch + 1}/{num_epochs}, Average Loss: {average_loss:.4f}")

# 测试模型
transformer_model.eval()
predictions = []
true_labels = []

with torch.no_grad():
    for batch_data, batch_labels in test_loader:
        batch_data, batch_labels = batch_data.to(device), batch_labels.to(device)
        batch_data = batch_data[:,:,12:16,12:16]
        # random_matrix = np.random.randint(-5, 6, size=(batch_size, 1, 4, 4))
        # data_type = torch.float32  # 例如，使用32位浮点数数据类型
        # batch_data = torch.Tensor(random_matrix).type(data_type)
        # batch_data = batch_data / 5

        # 使用CNN提取特征
        features = cnn_model(batch_data)
        features = features.view(features.size(0), -1)  # 展平特征
        # features = batch_data.view(64,784)

        logits = transformer_model(features)
        predicted_labels = torch.argmax(logits, dim=1).cpu().numpy()
        print(predicted_labels)
        predictions.extend(predicted_labels)
        true_labels.extend(batch_labels.cpu().numpy())

accuracy = accuracy_score(true_labels, predictions)
print(f"Test Accuracy: {accuracy:.2f}")
