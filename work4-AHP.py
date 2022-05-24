import numpy as np
import matplotlib.pyplot as plt

def weight(x):
    x1 = np.prod(x, axis=1)**(1/x.shape[0])
    sum = x1.sum()
    res = x1/sum
    return res.reshape(x.shape[0],1)
def getRI(num):
    if (num==1 or num==2):
        return 0
    elif (num==3):
        return 0.52
    elif (num==4):
        return 0.89
    elif (num==5):
        return 1.12
def check(x):
    n = x.shape[0]
    w = weight(x)
    Aw = np.dot(x, w)
    lamada = (Aw/w).sum()/n
    if(n==1 or n==2):
        CR = 0
    else:
        CI = (lamada - n) / (n - 1)
        RI = getRI(n)
        CR = CI / RI
    if(CR>0.1):
        print('一致性检验未通过❌')
    else:
        print('一致性检验通过✔')
    return CR
def draw(x,y):
    plt.figure(figsize=(8, 5))
    plt.barh(y, x)
    plt.title("暴雨内涝危害评价")
    plt.show()
if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    # A1 = np.array([[1,1/4,2,1/3],[4,1,8,2],[1/2,1/8,1,1/5],[3,1/2,5,1]])
    Alist = ['死亡人数','失踪人数','受伤人数','受灾人数','转移人数','直接经济损失','间接经济损失','城市交通影响','地铁交通影响','铁路交通影响','航班影响']
    A = np.array([[1, 3, 8], [1/3, 1, 3], [1/8, 1/3, 1]])
    B1 = np.array([[1, 3, 5, 8, 9],
                   [1/3, 1, 2, 4, 5],
                   [1/5, 1/2, 1, 2, 3],
                   [1/8, 1/4, 1/2, 1, 2],
                   [1/9, 1/5, 1/3, 1/2, 1]])
    B2 = np.array([[1, 6], [1/6, 1]])
    B3 = np.array([[1, 3, 7, 7],
                   [1/3, 1, 3, 3],
                   [1/7, 1/3, 1, 1],
                   [1/7, 1/3, 1, 1]])
    Aw = weight(A)
    print('Aw:', Aw)
    print(check(A))
    B1w = weight(B1)
    print('B1w:', B1w)
    print(check(B1))
    B2w = weight(B2)
    print('B2w:', B2w)
    print(check(B2))
    B3w = weight(B3)
    print('B3w:', B3w)
    print(check(B3))
    print('结果：-----------')
    A1 = B1w*Aw[0]
    A2 = B2w*Aw[1]
    A3 = B3w*Aw[2]
    # print(A1.flatten(),A2.flatten(),A3.flatten()))
    res = list(A1.flatten())+list(A2.flatten())+list(A3.flatten())
    print(res)
    print(A1.sum()+A2.sum()+A3.sum())
    draw(res, Alist)
