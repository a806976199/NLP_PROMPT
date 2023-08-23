# 测试泛化模型的能力

## 每种简称对应的类型

### data_large
- 元素种类  
（2种函数）* (8个历史序列预测4个,16个历史序列预测8个)
- 数量  
每组30000条数据 * 4
- 函数种类  
[x,Sin]  
[x,Cos,tri_poly,Sin]

### data_small
- 元素种类  
（2种函数）* (8个历史序列预测4个,16个历史序列预测8个)
- 数量  
每组10000条数据 * 2 * 2
- 函数种类  
[x,Sin]  
[x,Cos,tri_poly,Sin]

### mix\_1000\_16-80-4\_2-function
- 元素种类  
（2种函数）* (16个历史序列预测8个,...,80个历史序列预测40个,间隔4)
- 数量  
每组1000条数据 * 2 * 16
- 函数种类  
[x,Sin]  
[x,Cos,tri_poly,Sin]

### mix\_1000\_8-18-2\_4-func
- 元素种类  
（4种函数）* (8个历史序列预测4个,...,18个历史序列预测9个,间隔2)
- 数量  
每组1000条数据 * 4 * 5
- 函数种类  
[x,Sin]  
[x,Cos,tri_poly,Sin]  
[Cos,tri_poly,Sum,Sin]  
[Cos,tri_poly,Sum,square,Sin]

### mix\_5000\_16-80-4\_2-function
- 元素种类  
（2种函数）* (16个历史序列预测8个,...,80个历史序列预测40个,间隔4)
- 数量  
每组5000条数据 * 2 * 16
- 函数种类  
[x,Sin]  
[x,Cos,tri_poly,Sin]

### mix\_5000\_8-18-2\_4-func
- 元素种类  
（4种函数）* (8个历史序列预测4个,...,18个历史序列预测9个,间隔2)
- 数量  
每组5000条数据 * 4 * 5
- 函数种类  
[x,Sin]  
[x,Cos,tri_poly,Sin]  
[x,Cos,tri_poly,Sum,Sin]  
[x,Cos,tri_poly,Sum,square,Sin]

### mix\_4-4
- 元素种类  
（4种函数）* (8个历史序列预测4个,...,24个历史序列预测12个,间隔4)
- 数量  
每组10000条数据 * 4 * 4
- 函数种类  
[x,Sin]  
[x,Cos,tri_poly,Sin]  
[x,Cos,tri_poly,Sum,Sin]  
[x,Cos,tri_poly,Sum,square,Sin]

### zero\_model\_test
- 元素种类  
（8种函数）* (16个历史序列预测8个,...,80个历史序列预测40个,间隔4)
- 数量  
每组5000条数据 * 8 * 16
- 函数种类  
[x,Sin]  
[x,square]  
[x,log]  
[x,sqrt]  
[x,Cos,tri_poly,Sin]  
[x,Sin,square,log]  
[x,Cos,atan,sqrt]  
[x,Sin,Sum,square]  

### result-4-1-1
- 元素种类  
（1种函数）* (8个历史序列预测4个)
- 数量  
每组10000条数据 * 1 * 1
- 函数种类  
[x,Sin]  

### result-4-3-1
- 元素种类  
（1种函数）* (8个历史序列预测4个)
- 数量  
每组30000条数据 * 1 * 1
- 函数种类  
[x,Sin]  

### result-4-3-4
- 元素种类  
（1种函数）* (8个历史序列预测4个)
- 数量  
每组30000条数据 * 1 * 1
- 函数种类  
[x,Cos,tri_poly,Sin]  

### result-8-1-1
- 元素种类  
（1种函数）* (16个历史序列预测8个)
- 数量  
每组10000条数据 * 1 * 1
- 函数种类  
[x,Sin]  

### result-8-3-1
- 元素种类  
（1种函数）* (16个历史序列预测8个)
- 数量  
每组30000条数据 * 1 * 1
- 函数种类  
[x,Sin]  

### result-8-3-4
- 元素种类  
（1种函数）* (16个历史序列预测8个)
- 数量  
每组30000条数据 * 1 * 1
- 函数种类  
[x,Cos,tri_poly,Sin]  

### result-6-3-2
- 元素种类  
（1种函数）* (8个历史序列预测4个,16个历史序列预测8个)
- 数量  
每组10000条数据 * 1 * 2
- 函数种类  
[x,Sin]  

## mix\_5000\_2-func\_prompt1
- 元素种类  
（2种函数）* (16个历史序列预测8个,...,80个历史序列预测40个,间隔4)
- 数量  
每组5000条数据 * 2 * 16
- 函数种类  
[x,Sin]  
[x,Cos,tri_poly,Sin]
- 使用特殊的提示:不使用$符号,但是将序列变成(x_1,...,x_n),(y_1,...,y_n)来预测(y_{n+1},...,y_{n+m})

### mix\_5000\_4-func\_prompt1
- 元素种类  
（4种函数）* (8个历史序列预测4个,...,18个历史序列预测9个,间隔2)
- 数量  
每组5000条数据 * 4 * 5
- 函数种类  
[x,Sin]  
[x,Cos,tri_poly,Sin]  
[x,Cos,tri_poly,Sum,Sin]  
[x,Cos,tri_poly,Sum,square,Sin]
- 使用特殊的提示:不使用$符号,但是将序列变成(x_1,...,x_n),(y_1,...,y_n)来预测(y_{n+1},...,y_{n+m})

## mix\_5000\_2-func\_prompt2
- 元素种类  
（2种函数）* (16个历史序列预测8个,...,80个历史序列预测40个,间隔4)
- 数量  
每组5000条数据 * 2 * 16
- 函数种类  
[x,Sin]  
[x,Cos,tri_poly,Sin]
- 使用特殊的提示:最原始的提示,(x1,y1),...,(x_n,y_n).的形式进行预测(y_{n+1},...,y_{n+m})

### mix\_5000\_4-func\_prompt2
- 元素种类  ppap
（4种函数）* (8个历史序列预测4个,...,18个历史序列预测9个,间隔2)
- 数量  
每组5000条数据 * 4 * 5
- 函数种类  
[x,Sin]  
[x,Cos,tri_poly,Sin]  
[x,Cos,tri_poly,Sum,Sin]  
[x,Cos,tri_poly,Sum,square,Sin]
- 使用特殊的提示:最原始的提示,(x1,y1),...,(x_n,y_n).的形式进行预测(y_{n+1},...,y_{n+m})

## mix\_5000\_2-func\_prompt3
- 元素种类  
（2种函数）* (16个历史序列预测8个,...,80个历史序列预测40个,间隔4)
- 数量  
每组5000条数据 * 2 * 16
- 函数种类  
[x,Sin]  
[x,Cos,tri_poly,Sin]  
- 使用特殊的提示:4推1,3推2,2推3,...,直接推出所有结果  

### mix\_5000\_4-func\_prompt3
- 元素种类  
（4种函数）* (8个历史序列预测4个,...,18个历史序列预测9个,间隔2)
- 数量  
每组5000条数据 * 4 * 5
- 函数种类  
[x,Sin]  
[x,Cos,tri_poly,Sin]  
[x,Cos,tri_poly,Sum,Sin]  
[x,Cos,tri_poly,Sum,square,Sin]  
- 使用特殊的提示:4推1,3推2,2推3,...,直接推出所有结果  

## mix\_5000\_8-func\_prompt3
- 元素种类  
（8种函数）* (8个历史序列预测4个,...,18个历史序列预测9个,间隔2)
- 数量  
每组5000条数据 * 8 * 5
- 函数种类  
[Sin]  
[square]  
[log]  
[sqrt]  
[Cos,tri_poly,Sin]  
[Sin,square,log]  
[Cos,atan,sqrt]  
[Sin,Sum,square]  
- 使用特殊的提示:4推1,3推2,2推3,...,直接推出所有结果  


## mix\_5000\_2-func\_prompt4
- 元素种类  
（2种函数）* (16个历史序列预测8个,...,80个历史序列预测40个,间隔4)
- 数量  
每组5000条数据 * 2 * 16
- 函数种类  
[x,Sin]  
[x,Cos,tri_poly,Sin]  
- 使用特殊的提示:具有粗粒化的步骤预测结果  

### mix\_5000\_4-func\_prompt4
- 元素种类  
（4种函数）* (8个历史序列预测4个,...,18个历史序列预测9个,间隔2)
- 数量  
每组5000条数据 * 4 * 5
- 函数种类  
[x,Sin]  
[x,Cos,tri_poly,Sin]  
[x,Cos,tri_poly,Sum,Sin]  
[x,Cos,tri_poly,Sum,square,Sin]  
- 使用特殊的提示:具有粗粒化的步骤预测结果  

## mix\_5000\_8-func\_prompt4
- 元素种类  
（8种函数）* (8个历史序列预测4个,...,18个历史序列预测9个,间隔2)
- 数量  
每组5000条数据 * 8 * 5
- 函数种类  
[Sin]  
[square]  
[log]  
[sqrt]  
[Cos,tri_poly,Sin]  
[Sin,square,log]  
[Cos,atan,sqrt]  
[Sin,Sum,square]  
- 使用特殊的提示:具有粗粒化的步骤预测结果  


## temp
## 泛化性能测试  

### zero\_shot\_test1(ok)
- 使用具有result-8-3-4的结果去预测result-4-3-4
- 这个实验是对预测长度的泛化能力的测试,即能够预测16-8的能力能否泛化到预测一个8-4的能力。

### zero\_shot\_test2(ok)
- 使用具有result-8-3-4的结果去预测result-8-3-1
- 这个实验是对函数种类(简单对复杂)的泛化能力的测试，即能够预测[x,sin(x)]函数的模型，能否预测[x,Cos,tri_poly,Sin]函数模型。
  
### zero\_shot\_test3(ok)
- 使用具有result-8-3-1的结果去预测result-8-3-4
- 这个实验是对函数种类(复杂对简单)的泛化能力的测试，即能够预测函数[x,Cos,tri_poly,Sin]的模型，能否预测[x,sin(x)]函数模型.

### zero\_shot\_test4(ok)
- 使用具有mix\_5000\_8-18-2\_4-func的结果去预测mix\_5000\_16-80-4\_2-function
- 具有大型能力的模型之间的相互预测,目的是测试函数种类多，序列种类少这两种模型哪种泛化能力的效果更好。

### zero\_shot\_test5(ok)
- 使用具有data_large去预测mix\_5000\_16-80-4\_2-function中的内容
- 目的是测试是否训练足够多的数量以后可以得到更好的泛化能力。

### zero\_shot\_test6(ok)
-  使用具有mix\_4-4去预测mix\_5000\_16-80-4\_2-function中的内容
-  是否数量少点，但是种类多点的结果的泛化能力更好？


### zero\_shot\_test7(ok)
-  使用具有zero\_model\_test去预测mix\_5000\_16-80-4\_2-function中的内容
-  是否一个更加综合的模型能够对结果有更强的泛化能力？

### zero\_shot\_test8()
- 使用修改的提示的模型zero\_model\_test_best-prompt 来预测一下mix\_5000\_16-80-4\_2-function的内容
- 验证泛化能力,使用新的机子来进行验证吧.

### zero\_shot\_test9()
- 使用修改的提示的模型mix\_5000\_8-18-2\_4-func_best-prompt 来预测一下mix\_5000\_16-80-4\_2-function的内容
- 验证泛化能力.


### mix\_1000\_8-18-2\_4-func_best-prompt(已经用服务器ok了,但是还没做泛化的测试)
- 元素种类  
（4种函数）* (8个历史序列预测4个,...,18个历史序列预测9个,间隔2)
- 数量  
每组1000条数据 * 4 * 5
- 函数种类  
[x,Sin]  
[x,Cos,tri_poly,Sin]  
[Cos,tri_poly,Sum,Sin]  
[Cos,tri_poly,Sum,square,Sin]
- 目的:
快速做个对比实验,看看效果怎么样.

### mix\_5000\_8-18- 2\_4-func_best-prompt(已经训练完成了,但是需要做泛化性和普通的实验)
- 元素种类  
（4种函数）* (8个历史序列预测4个,...,18个历史序列预测9个,间隔2)
- 数量  
每组5000条数据 * 4 * 5
- 函数种类  
[x,Sin]  
[x,Cos,tri_poly,Sin]  
[x,Cos,tri_poly,Sum,Sin]  
[x,Cos,tri_poly,Sum,square,Sin]

- 目的:  
这个实验的目的是为了对比之前使用了$符号,且修改了elements的情况
- 需要将内容跑完,评估自己数据集的预测结果,预测未来mix\_5000\_16-80-4\_2-function新的预测的结果.


### zero\_model\_test_best-prompt (这个已经训练好了,泛化性能的预测是可以快速搞定,普通实验不做了,没意义了.)
- 元素种类  
（8种函数）* (16个历史序列预测8个,...,80个历史序列预测40个,间隔4)
- 数量  
每组5000条数据 * 8 * 16
- 函数种类  
[x,Sin]  
[x,square]  
[x,log]  
[x,sqrt]  
[x,Cos,tri_poly,Sin]  
[x,Sin,square,log]  
[x,Cos,atan,sqrt]  
[x,Sin,Sum,square]  

- 目的:  
这个实验的目的是通过对比使用新的提示方式得到的泛化模型,和前面的最宽广的模型在泛化能力上的比较,以及普通预测的能力的比较
- 将这个实验跑完,并估计自己的结果,预测未来mix\_5000\_16-80-4\_2-function新的预测的结果.



### mix\_1000\_8-18-2\_4-func_best-prompt_chatglm2(有问题,不做了)
- 元素种类  
（4种函数）* (8个历史序列预测4个,...,18个历史序列预测9个,间隔2)
- 数量  
每组1000条数据 * 4 * 5
- 函数种类  
[x,Sin]  
[x,Cos,tri_poly,Sin]  
[Cos,tri_poly,Sum,Sin]  
[Cos,tri_poly,Sum,square,Sin]
- 目的:
和chatglm1做对比实验,包括泛化性能和普通的性能.

### mix\_5000\_8-18-2\_4-func_best-prompt_chatglm2(差评估)
- 元素种类  
（4种函数）* (8个历史序列预测4个,...,18个历史序列预测9个,间隔2)
- 数量  
每组5000条数据 * 4 * 5
- 函数种类  
[x,Sin]  
[x,Cos,tri_poly,Sin]  
[x,Cos,tri_poly,Sum,Sin]  
[x,Cos,tri_poly,Sum,square,Sin]

- 目的:  
和chatglm1做对比实验,包括泛化性能和普通的性能.
- 需要将内容跑完,评估自己数据集的预测结果,预测未来mix\_5000\_16-80-4\_2-function新的预测的结果.

### zero\_model\_test_best-prompt_chatglm2(有问题不做了)
- 元素种类  
（8种函数）* (16个历史序列预测8个,...,80个历史序列预测40个,间隔4)
- 数量  
每组5000条数据 * 8 * 16
- 函数种类  
[x,Sin]  
[x,square]  
[x,log]  
[x,sqrt]  
[x,Cos,tri_poly,Sin]  
[x,Sin,square,log]  
[x,Cos,atan,sqrt]  
[x,Sin,Sum,square]  
- 目的:
和chatglm1做对比实验,包括泛化性能和普通的性能.

## 目前要做的实验

### mix_5000_4-func_prompt3
使用mix_5000_4-func_prompt3以及mix_5000_2-func_prompt3数据集合来验证这个提示的效果
- 目的:通过使用特殊提示3,看最终效果
- 结果:  
见过的任务测试因为选择的区域太短,导致还没完美测试(ok)
对于泛化性测试更加没做过.(ok)

### mix_5000_4-func_prompt4
使用mix_5000_4-func_prompt4以及mix_5000_2-func_prompt4数据集合来验证这个提示的效果
- 目的:通过使用特殊提示4,看最终效果
- 结果:  
见过的任务测试还在考虑中(ok)
对于泛化性测试更加没做过(ok)

<!-- ### mix_5000_4-func_prompt5 -->
<!-- 使用mix_5000_4-func_prompt5以及mix_5000_2-func_prompt5数据集合来验证这个提示的效果 -->
<!-- - 目的:通过使用特殊提示5,看最终效果 -->
<!-- - 结果:   -->
<!-- 见过的任务测试还在考虑中(ing).   -->
<!-- 对于泛化性测试更加没做过(ing).   -->

### mix_5000_8-func_promp3
泛化任务（ok）
普通任务（ok）

### mix_5000_8-func_promp4
泛化任务（ok）
普通任务（ok）


## test3

### 测试了一下如何使用新的提示混合体-3000
普通任务（ok）
泛化任务1（ing）
<!-- 泛化任务2 (用其他的结果来对比测试一下，8-func_prompt4) -->


## test2

### mix_5000_8-func_prompt4-a 3000
- 将序列预测改成x预测x,而不是之前的x预测x/2
- 普通任务（ok）
- 泛化任务（同样的泛化任务测试）

### mix_5000_8-func_prompt4-b 3000
- 虽然是x预测x/2，但是增加了更多不同长度的序列。
- 普通任务（ok）
- 特殊任务（同样的泛化任务测试）

## test1

### 添加Revin,或者特殊的小波变换以后的测试结果,看看是否有更好的效果  1400
普通任务  （ok）
泛化任务  （not ok,有难度）

### 对比测试组,单纯使用简单的不使用粗粒化的方法结果对比组  1400
训练（ok）
普通任务 （ok）
泛化任务 （no ok，有难度）

###  使用特殊的auto-cot试试看！

