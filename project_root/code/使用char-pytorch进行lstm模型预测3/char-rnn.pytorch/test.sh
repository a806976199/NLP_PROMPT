#将所有文件进行训练并保存到相应的文件夹里面
# 运行脚本
for file in ../filter_data/*; do
    python  train.py \
    	    --model lstm \
    	    --n_epochs 3000 \
    	    --batch_size 50  \
    	    $file
done
