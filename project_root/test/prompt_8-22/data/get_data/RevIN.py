import torch
import torch.nn as nn

class RevIN(nn.Module):
    def __init__(self, num_features: int, eps=1e-5, affine=True):
        """
        :param num_features: the number of features or channels
        :param eps: a value added for numerical stability
        :param affine: if True, RevIN has learnable affine parameters
        """
        super(RevIN, self).__init__()
        self.num_features = num_features
        self.eps = eps
        self.affine = affine
        if self.affine:
            self._init_params()

    def forward(self, x, mode:str):
        if mode == 'norm':
            self._get_statistics(x)
            x = self._normalize(x)
        elif mode == 'denorm':
            x = self._denormalize(x)
        else: raise NotImplementedError
        return x

    def _init_params(self):
        # initialize RevIN params: (C,)
        self.affine_weight = nn.Parameter(torch.ones(self.num_features))
        self.affine_bias = nn.Parameter(torch.zeros(self.num_features))

    def _get_statistics(self, x):
        dim2reduce = tuple(range(1, x.ndim-1))
        self.mean = torch.mean(x, dim=dim2reduce, keepdim=True).detach()
        self.stdev = torch.sqrt(torch.var(x, dim=dim2reduce, keepdim=True, unbiased=False) + self.eps).detach()

    def _normalize(self, x):
        x = x - self.mean
        x = x / self.stdev
        if self.affine:
            # own weight
            # print(x)
            # print(x.shape)
            # print(self.affine_weight.shape)
            # print(self.affine_weight)
            # affine_weight = self.affine_weight.unsqueeze(0).unsqueeze(-1)
            # affine_weight = affine_weight.expand(x.shape[0],-1,x.shape[-1])
            # print(affine_weight.shape)
            # print(affine_weight)
            # x = x * affine_weight
            # #own bias
            # print(self.affine_bias)
            # print(self.affine_bias.shape)
            # affine_bias = self.affine_bias.unsqueeze(0).unsqueeze(-1)
            # affine_bias = affine_bias.expand(x.shape[0],-1,x.shape[-1])
            # x = x + affine_bias

            x = x * self.affine_weight
            x = x + self.affine_bias
        return x

    def _denormalize(self, x):
        if self.affine:
            x = x - self.affine_bias
            x = x / (self.affine_weight + self.eps*self.eps)
        x = x * self.stdev
        x = x + self.mean
        return x


# # 创建 RevIN 模块
# num_features = 3
# revin = RevIN(num_features)

# # 创建随机输入张量
# batch_size = 1
# sequence_length = 10
# input_channels = num_features
# #input_tensor = torch.randn(batch_size, input_channels, sequence_length)
# #input_tensor = torch.randn(input_channels)
# input_tensor = torch.tensor([1,2,3]).float()
# print(input_tensor)
# print(input_tensor.shape)
# # 标准化
# normalized_tensor = revin(input_tensor, mode='norm')

# # 反标准化
# denormalized_tensor = revin(normalized_tensor, mode='denorm')

# print("原始输入张量：\n", input_tensor)
# print("标准化后的张量：\n", normalized_tensor)
# print("反标准化后的张量：\n", denormalized_tensor)
# print(test)
