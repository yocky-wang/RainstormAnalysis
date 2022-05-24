# -*- coding: utf-8 -*-
import jieba
import re
import os
import pandas as pd
from sklearn import feature_extraction, linear_model, model_selection
from sklearn.metrics import f1_score, classification_report

# count_vectorizer = feature_extraction.text.CountVectorizer()
def stopwordslist(filepath):  # 定义函数创建停用词列表
    stopword = [line.strip() for line in open(filepath, 'r', encoding="UTF-8").readlines()]  # 以行的形式读取停用词表，同时转换为列表
    return stopword

def getdata(filepath):
    data = []
    target = []

    dirs = os.listdir(filepath)
    for dirr in dirs:
        files = os.listdir(filepath + dirr)
        for file in files:
            filename = filepath + dirr + '/' + file
            print(filename)
            try:
                with open(filename, 'rb') as fp:
                    content1 = fp.read().decode('utf-8')
                    content2 = content1.replace(' ', '')  # 去掉文本中的空格
                    # print('\n【去除空格后的文本：】' + '\n' + content1)
                    pattern = re.compile("[^\u4e00-\u9fa5]")
                    content3 = re.sub(pattern, '', content2)
            except :
                message = "Sorry, the file " + filename + " does not exist."
                print(message)
            else:
                target.append(1 if dirr == 'positive' else 0)
                data.append(content3)
    return data, target


if __name__ == '__main__':
    stopwords_filepath = "./stopwords.txt"
    train_filepath = "./train/"
    test_filepath = "./test/"

    train_data, train_target = getdata(train_filepath)
    test_data, test_target = getdata(test_filepath)

    #####
    # stopwords = stopwordslist(stopwords_filepath) #停用词表
    train_data = [" ".join(jieba.lcut(e)) for e in train_data]
    test_data = [" ".join(jieba.lcut(e)) for e in test_data]
    print(len(train_data))
    print(len(train_target))
    # print(train_target)
    print('----------------')
    print(len(test_data))
    print(len(test_target))
    # print(test_target)
    # count_vectorizer = feature_extraction.text.CountVectorizer(stop_words=stopwords)
    count_vectorizer = feature_extraction.text.CountVectorizer()
    train_vectors = count_vectorizer.fit_transform(train_data)
    test_vectors = count_vectorizer.transform(test_data)
    # train_target = pd.DataFrame(train_target)
    # print(count_vectorizer.get_feature_names())

    clf = linear_model.RidgeClassifier()
    # scores = model_selection.cross_val_score(clf, train_vectors, train_target, cv=3, scoring="f1")
    # print(scores)
    clf.fit(train_vectors, train_target)
    labels=['negative', 'positive']
    print(classification_report(test_target, clf.predict(test_vectors), target_names=labels))

    print('start---------')
    basepaths = './百度下载的网页'
    basepath = os.listdir(basepaths)
    testdata=[]
    prefile=[]
    for dir1 in basepath:
        filename = os.listdir(basepaths+'/'+dir1)
        for dir2 in filename:
            testpaths = basepaths+'/'+dir1+'/'+dir2
            # print(testname) #./百度下载的网页/京津冀/保定
            testlist = os.listdir(testpaths)
            for dir3 in testlist:
                testpath = testpaths+'/'+dir3 #./百度下载的网页/京津冀/保定/0.html
                try:
                    with open(testpath, 'rb') as fp:
                        content1 = fp.read().decode("utf8","ignore")
                        content2 = content1.replace(' ', '')
                        pattern = re.compile("[^\u4e00-\u9fa5]")
                        content3 = re.sub(pattern, '', content2)
                except Exception as e:
                    message = "Sorry, the file " +testpath+ " does not exist."
                    print(message,e)
                else:
                    prefile.append(testpath)
                    testdata.append(content3)
    testdata = [" ".join(jieba.lcut(e)) for e in testdata]
    testvectors = count_vectorizer.transform(testdata)
    test_pre = clf.predict(testvectors)
    print(test_pre[:10])
    print(prefile[:10])
    print('end---------')


