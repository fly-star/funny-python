'''
1.输入一个由int组成的list,[x1,x2,x3...],计算出x1^(x2^(x3^(...^xn)))的值的最后一位数字
'''

def rehh(lists):
    from functools import reduce
    a, *b = lists
    b = b[::-1]
    res = pow(a, reduce(lambda x, y: pow(y, x), b, 1))
    return res, str(res)[-1]
