def getScore(death, missing, injured, victims, transfers, economic1, economic2, traffic, subway, train, flight):
    score = []
    l1 = lambda a : 0 if a==0 else 40 if a>=1 and a<=2 else 60 if a>=3 and a<=9 else 80 if a>=10 and a<=29 else 100
    score.append(l1(death))
    score.append(l1(missing))
    score.append(0 if injured==0 else 40 if injured>=1 and injured<=9 else 60 if injured>=10 and injured<=49 else 80 if injured>=50 and injured<= 99 else 100)
    score.append(20 if victims<2E+4 else 40 if victims>=2E+4 and victims<1E+5 else 60 if victims>=1E+5 and victims<5E+5 else 80 if victims>=5E+5 and victims<1E+6 else 100)
    score.append(20 if transfers < 1E+3 else 40 if transfers >= 1E+3 and transfers < 5E+3 else 60 if transfers >= 5E+3 and transfers < 2E+4 else 80 if transfers >= 2E+4 and transfers < 5E+4 else 100)
    score.append(40 if economic1 < 5E+6 else 60 if economic1 >= 5E+6 and economic1 < 1E+7 else 80 if economic1 >= 1E+7 and economic1 < 5E+7 else 100)
    score.append(40 if economic2 < 5E+6 else 60 if economic2 >= 5E+6 and economic2 < 1E+7 else 80 if economic2 >= 1E+7 and economic2 < 5E+7 else 100)
    score.append(40 if traffic=='严重' else 60 if traffic=='比较严重' else 80 if traffic=='非常严重' else 100)
    score.append(0 if subway=='否' else 100)
    score.append(0 if train == '否' else 100)
    score.append(0 if flight == '否' else 100)
    return score
if __name__ == '__main__':
    AHP = [0.3699033528837416, 0.15360001711826454, 0.08261021773908417, 0.04574814838811123, 0.029862816383510713,
           0.2025777447798559, 0.03376295746330932, 0.04976962863573782, 0.018811151459171588, 0.006676982574606542,
           0.006676982574606542]
    # 北京7.21暴雨
    scoreList = getScore(71, 8, 1309, 1.9E+7, 56933, 1.164E+10, 2.328E+10, '非常严重', '是', '是', '是')
    score = 0
    for i in range(0, 11):
        score += AHP[i] * scoreList[i]
    print(score)  # 92.86060674255467
    level = '轻度' if score <= 40 else '中度' if score > 40 and score <= 60 else '严重' if score > 60 and score <= 80 else '特大'
    print(level)