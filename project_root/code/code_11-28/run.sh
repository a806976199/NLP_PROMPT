# 训练脚本
# test_name='math-BIML'
# nepochs=400
# python train.py \
#        --episode_type algebraic+biases \
#        --fn_out_model $test_name$nepochs'.pt' \
#        --nepochs $nepochs \
#        --batch_size 2  > $test_name$nepochs'.txt'


#> $test_name'.txt'
# 评估脚本
# python eval.py  \
#        --max \
#        --episode_type few_shot_gold \
#        --fn_out_modelsehll net-BIML-top.pt \
#        --verbose

#评估脚本
#python -m pdb eval.py --batch_size 2 --max --episode_type few_shot_gold --fn_out_model small-BIML.pt --verbose 

#测试简单的训练脚本,并尝试进行修改一波.
test_name='my_test'
nepochs=5
#python -m pdb train.py \
python train.py \
       --episode_type algebraic+biases \
       --fn_out_model $test_name$nepochs'.pt' \
       --nepochs $nepochs \
       --batch_size 2 

#测试简单的测试脚本
# python eval.py --batch_size 2 --max --episode_type few_shot_gold --fn_out_model $test_name$nepochs'.pt' --verbose

# rm out_models/$test_name$nepochs'.pt' 
