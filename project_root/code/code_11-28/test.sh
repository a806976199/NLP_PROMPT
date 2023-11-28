
# 评估脚本
# model_name='small-BIML'
# python -m pdb eval.py --batch_size 2 --max --episode_type few_shot_gold --fn_out_model $model_name'.pt' --verbose
# 评估脚本
model_name='math-BIML400'
python -m pdb  eval.py --batch_size 2 --max --episode_type few_shot_gold --fn_out_model $model_name'.pt' --verbose

#> $model_name'_eval.txt'

# model_name='small-BIML100'

# python eval.py --batch_size 2 --max --episode_type few_shot_gold --fn_out_model $model_name'.pt' --verbose  > $model_name'_eval.txt'

# model_name='small-BIML200'

# python eval.py --batch_size 2 --max --episode_type few_shot_gold --fn_out_model $model_name'.pt' --verbose  > $model_name'_eval.txt'

# model_name='middle-BIML'

# python eval.py --batch_size 2 --max --episode_type few_shot_gold --fn_out_model $model_name'.pt' --verbose  > $model_name'_eval.txt'

# model_name='middle-BIML100'

# python eval.py --batch_size 2 --max --episode_type few_shot_gold --fn_out_model $model_name'.pt' --verbose  > $model_name'_eval.txt'

# model_name='middle-BIML200'

# python eval.py --batch_size 2 --max --episode_type few_shot_gold --fn_out_model $model_name'.pt' --verbose  > $model_name'_eval.txt'

# model_name='net-BIML'

# python eval.py --batch_size 2 --max --episode_type few_shot_gold --fn_out_model $model_name'.pt' --verbose  > $model_name'_eval.txt'


