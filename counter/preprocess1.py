import pandas as pd
import re
import jieba
import jieba.posseg

# Preprocess data by lowing letters, deleting numbers, cutting words simply, deleting stopwords and extra spaces, result is a string.
def preprocess_base(text_data):
    text_data = text_data.lower()
    text_data = re.sub('\d+', '', text_data)
    text_data = re.sub('\'', '', text_data)
    text_data = re.sub('-', '', text_data)
    text_data = re.sub('%', '', text_data)
    text_data = re.sub('\.', '', text_data)
    text_data = re.sub('\"', '', text_data)
    text_data = re.sub('_', '', text_data)
    text_data = re.sub('#', '', text_data)
    text_data = re.sub('δ', '', text_data)
    text_data = re.sub('ő', '', text_data)
    text_data = re.sub('&', '', text_data)
    text_data = re.sub('ｙ', '', text_data)
    if judge == 'simple': text_data = jieba.lcut(text_data)
    else: text_data = jieba.posseg.cut(text_data)
    text_data = [word.strip() for word in text_data if word not in stopwords.text.values]
    text_data = " ".join(text_data)
    return text_data

if __name__ == '__main__':
    trainset = pd.read_csv('../dataset/test_3/train.csv', sep =',', header = None, names = ['label', 'text'])
    trainset.drop(0, inplace = True)
    valset = pd.read_csv('../dataset/test_3/val.csv', sep =',', header = None, names = ['label', 'text'])
    valset.drop(0, inplace = True)
    testset = pd.read_csv('../dataset/test_3/test.csv', sep =',', header = None, names = ['label', 'text'])
    testset.drop(0, inplace = True)
    stopwords = pd.read_csv('../dataset/stopwords/stopwords.txt', header = None, names = ['text'], error_bad_lines=False, engine='python', encoding ='utf-8')
    judge = 'simple'
    print('************开始处理训练集************')
    trainset['cuttedtext'] = trainset.text.apply(preprocess_base)
    print('***********************************')
    print('************开始处理验证集************')
    valset['cuttedtext'] = valset.text.apply(preprocess_base)
    print('***********************************')
    print('************开始处理测试集************')
    testset['cuttedtext'] = testset.text.apply(preprocess_base)
    print('***********************************')
    labelMap = {'1': 0, '2': 1, '4': 2}
    trainset['changedlabel'] = trainset['label'].map(labelMap)
    valset['changedlabel'] = valset['label'].map(labelMap)
    testset['changedlabel'] = testset['label'].map(labelMap)
    trainset[['changedlabel','cuttedtext']].to_csv('../dataset/test_3/train_pre.csv',index=False)
    valset[['changedlabel', 'cuttedtext']].to_csv('../dataset/test_3/val_pre.csv', index=False)
    testset[['changedlabel', 'cuttedtext']].to_csv('../dataset/test_3/test_pre.csv', index=False)