import math


#身長を掛け算で大きくする関数
def multipleHeight(original, number = 2):
    #小数点以下を切り捨て
    return math.floor(int(original) * number)
