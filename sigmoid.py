import numpy as np

def sigmoid(t):
    '''
    完成sigmoid函数计算
    :param t: 负无穷到正无穷的实数
    :return: 转换后的概率值
    '''
    #********** Begin **********#
    return 1 / (1 + np.exp(-t))
    #********** End **********#

# 调用函数
#********** Begin **********#
print("sigmoid(1) =", sigmoid(1))     # 预期输出：0.73105857863
print("sigmoid(-2) =", sigmoid(-2))   # 预期输出：0.119202922022
#********** End **********#

