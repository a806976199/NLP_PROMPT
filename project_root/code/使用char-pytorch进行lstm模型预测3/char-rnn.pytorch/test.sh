#file='filter_data/AAAU.csv'
#将所有文件进行训练并保存到相应的文件夹里面

python  train.py \
    	--model lstm \
    	--n_epochs 3000 \
    	--batch_size 50  \
    	filter_data/AGR.csv

python  train.py \
    	--model lstm \
    	--n_epochs 3000 \
    	--batch_size 50  \
    	filter_data/AMD.csv

python  train.py \
    	--model lstm \
    	--n_epochs 3000 \
    	--batch_size 50  \
    	filter_data/BAH.csv

python  train.py \
    	--model lstm \
    	--n_epochs 3000 \
    	--batch_size 50  \
    	filter_data/BKR.csv

python  train.py \
    	--model lstm \
    	--n_epochs 3000 \
    	--batch_size 50  \
    	filter_data/IBTD.csv

python  train.py \
    	--model lstm \
    	--n_epochs 3000 \
    	--batch_size 50  \
    	filter_data/IGF.csv

# 训练脚本
