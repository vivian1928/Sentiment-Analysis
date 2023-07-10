if __name__ == '__main__':
    # baidu_stopwords = set(open('../dataset/stopwords/baidu_stopwords.txt', encoding='utf-8').readlines())
    # cn_stopwords = set(open('../dataset/stopwords/cn_stopwords.txt', encoding='utf-8').readlines())
    # hit_stopwords = set(open('../dataset/stopwords/hit_stopwords.txt', encoding='utf-8').readlines())
    # scu_stopwords = set(open('../dataset/stopwords/scu_stopwords.txt', encoding='utf-8').readlines())
    all_stopwords = set(open('../dataset/stopwords/all_stopwords.txt', encoding='utf-8').readlines())
    other_stopwords = set(open('../dataset/stopwords/filter.txt', encoding='utf-8').readlines())
    # union_stopwords = baidu_stopwords | cn_stopwords | hit_stopwords | scu_stopwords
    # sub_stopwords = all_stopwords - union_stopwords
    union_stopwords = all_stopwords | other_stopwords
    # print(sub_stopwords)
    f = open("../dataset/stopwords/stopwords.txt", "w", encoding='utf-8')
    f.writelines(union_stopwords)
    f.close()