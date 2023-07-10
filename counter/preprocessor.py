import jieba
from tqdm import tqdm
import pandas as pd
import os

# jieba.load_userdict("../dataset/1000000-dict.txt")

"去除指定无用的符号"
puncts = [' ', '\'', '\"', '-', '.']
def clean_text(x):
    x = x.strip()
    for punct in puncts:
        x = x.replace(punct,'')
    return x

"让文本只保留汉字、英文和数字"
def is_chinese_alphabet_number(xchar):
    if (xchar >= u'\u4e00' and xchar <= u'\u9fa5') or (xchar >= u'\u0030' and xchar <= u'\u0039') or (xchar >= u'\u0041' and xchar <= u'\u005a') or (xchar >= u'\u0061' and xchar <= u'\u007a'):
        return True
    else:
        return False
"将汉字、英文和数字保留下来"
def keep_text(x):
    out_str=''
    for i in x:
        if is_chinese_alphabet_number(i):
            out_str = out_str+i
    return out_str

def seg_sentence(sentence,stopwords):
    "对句子进行分词和去除停用词"
    jieba.load_userdict("../dataset/user_dict.txt")
    sentence_lower = sentence.lower()
    sentence_seged = jieba.cut(sentence_lower, cut_all=False)
    outstr=''
    for word in sentence_seged:
        if word not in stopwords:
                outstr+=word
                outstr+=" "
    return outstr

def build_vocab(sentences,verbose=True):
    "追踪训练词汇表，遍历所有文本对单词进行计数"
    vocab={}
    for sentence in tqdm(sentences,disable=(not verbose)):
        for word in sentence.split():
            try:
                vocab[word] += 1
            except KeyError:
                vocab[word] = 1

    return vocab

# def texts_to_sequences(sentences,vocab,verbose=True):
#     seq_sentences=[]
#     unk_vec=np.random.random(embed_size)*0.5
#     unk_vec=unk_vec-unk_vec.mean()
#     for sentence in tqdm(sentences,disable=(not verbose)):
#         seq_sentence=[]
#         for word in sentence.split():
#             seq_sentence.append(vocab.get(word,unk_vec))
#         seq_sentences.append(seq_sentence)
#     return seq_sentences

def load_and_prec():
    #文件读取
    dataset = pd.read_csv('../dataset/dataset.csv')
    #创建停用词列表
    stopwords = ['的', '呀', '这', '那', '就', '的话', '如果', '了', '建议', '说','是', '吧','我','你','在','这个','被','啊','和','吗','觉得','就是','应该','认为','很','感觉','可能','会','下面']
    #创建自定义词表
    dataset["content"]=dataset["content"].apply(lambda x: clean_text(x))
    dataset["content"]=dataset["content"].apply(lambda x: keep_text(x))
    dataset["content"]=dataset["content"].apply(lambda x: seg_sentence(x, stopwords))
    dataset.to_csv('../dataset/pre_dataset.csv', index = False)
    return dataset

if __name__ == '__main__':
    vocab_size = 100
    if not os.path.exists('../dataset/pre_dataset.csv') :
        dataset = load_and_prec()
    else:
        dataset = pd.read_csv('../dataset/pre_dataset.csv')
        for item in dataset['content']:
            print(item)
            if item == None:
                item = ''
    print(dataset["content"][0])
    vocab = build_vocab(dataset["content"],True)
    vocabtmp = sorted(vocab.items(),key=lambda d:d[1],reverse=True)   # 分词后共出现73915个单词
    vocab_100 = vocabtmp[:vocab_size]
    # # split to train and val
    # dataset, test_df = train_test_split(dataset, test_size=0.01, random_state=2019)
    # dataset,val_df=train_test_split(dataset,test_size=0.01,random_state=2019)
    #
    # # print("Train shape: ",dataset.shape)   # (34623, 3)
    # # print("Val shape: ",val_df.shape)   # (3848, 3)
    #
    # ## Get the input values
    # train_X=dataset["text"].values
    # val_X=val_df["text"].values
    # test_X=test_df["text"].values
    #
    # ## Get the target values
    # train_y=dataset["label"].values
    # val_y=val_df["label"].values
    # test_y=test_df["label"].values
    #
    # np.random.seed(2019)
    # trn_idx=np.random.permutation(len(train_X))
    # val_idx=np.random.permutation(len(val_X))
    #
    # train_X=train_X[trn_idx]
    # val_X=val_X[val_idx]
    # train_y=train_y[trn_idx]
    # val_y=val_y[val_idx]
    #
    # # Tokenize the sentences
    # train_X=texts_to_sequences(train_X, vocab)
    # val_X=texts_to_sequences(val_X,vocab)
    # test_X=texts_to_sequences(test_X,vocab)
    # # Pad the sentences
    # train_X=pad_sequences(train_X,maxlen=maxlen)
    # val_X=pad_sequences(val_X,maxlen=maxlen)
    # test_X=pad_sequences(test_X,maxlen=maxlen)
    #
    # return dataset,test_df,train_X,val_X,test_X,train_y,val_y,test_y,vocab