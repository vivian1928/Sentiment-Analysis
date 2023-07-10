if __name__ == '__main__':
    words = open('../dataset/1000000-dict.txt', encoding='utf-8').readlines()
    print(words[0])
    words_jieba = []
    for line in words:
        tmp = line.replace('\n', '')
        tmp = tmp + ' ' + '3' + ' ' + 'n' + '\n'
        words_jieba.append(tmp)
    print(words_jieba[0])
    f = open('../dataset/1000000-dict-jieba.txt', 'w' , encoding='utf-8')
    f.writelines(words_jieba)
    f.close()