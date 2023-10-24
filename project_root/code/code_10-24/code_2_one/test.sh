 #将所有文件进行训练并保存到相应的文件夹里面
for file in filter_data/*; do
    python  train.py \
    	    --model lstm \
    	    --n_epochs 1000 \
    	    --batch_size 50  \
	    --cuda \
    	    $file
done


#for file in filter_data/*; do
# for file in $(ls -r filter_data/*); do

# done
#python -m pdb train.py \
# python  train.py \
#        --model lstm \
#        --n_epochs 10 \
#        --batch_size 30  \
#        --cuda  \
#        filter_data/A.csv

