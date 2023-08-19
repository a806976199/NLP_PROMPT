# 部署chatglm-6b模型

## 具体步骤

### 进入服务器然后创建一个新的环境(可以使用venv或者anaconda创建新的环境)  
- 创建一个python新环境,python的版本最好使用3.8版本及以上的版本,用conda或者venv创建一个新的python环境.比如使用conda创建新环境:  
```  
conda create -name myenv(环境名) python=3.8  
conda activate myenv
```  

### 从guthub上下载chatglm-6b代码,并安装需要的第三方包  
```   
git clone https://github.com/THUDM/ChatGLM-6B.git  
cd ChatGLM-6B  
pip install -r requirements.txt
```

### 从huggingface中下载chatglm-6b的预训练模型,但这边下载需要vpn才可以.(这边还可以下载到其他开源模型)
[预训练模型下载入口(需要vpn)](https://huggingface.co/THUDM/chatglm-6b/tree/main)

### 选择预训练模型,以及训练的数据集合

- 修改训练模型脚本train.sh,评估模型脚本evaluate.sh  
上面这个最初的train.sh的内容,其中我们需要修改的是预训练模型的路径,将默认的
```  
THUDM/chatglm-6b
```
改成我们从huggingface中下载的预训练模型chatglm-6b的路径.比如我放在了ChatGLM-6B文件夹里面里面,就可以将默认路径改成
```  
../chatglm-6b
```
- 确定训练的数据集  
上面的AdvertiseGen放到默认的用于训练的数据集train.json和用于验证的数据集dev.json可以自行修改我们自己的数据集.但是github上刚下载的code没有AdvertiseGen文件夹以及里面的数据,可以将我发的AdvertiseGen文件夹放入ptuning文件夹里面.

### 修改main.py 文件代码
- 在main.py文件的第48行里面添加下面这一行代码,wandb这个工具第一次使用需要注册并且输入密钥,如果没有密钥容易报错导致程序运行失败,所以直接禁用即可.  
```   
os.environ["WANDB_DISABLED"] = "true"
```

- 代码的运行:  

 在ptuning文件夹里面运行如下命令来进行模型训练  
```
	bash train.sh
```  
训练完以后使用运行如下命令进行模型评估  
```
	bash evaluate.sh
```  
- 结果可以在output文件夹里面进行查看

## chatglm模型进行训练和评估基本完成.至于其他根据自己的需要可在mian.py里面进行微调.


## 注意事项:
- 服务器里面可能无法下载上述chatglm-6b代码,以及chatglm-6b模型,最好在自己电脑上将这些代码下载下来,然后使用scp命令复制到服务器上.
