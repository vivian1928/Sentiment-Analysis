import pandas as pd

def is_chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

def is_number(uchar):
    if uchar >= u'\u0030' and uchar <= u'\u0039':
        return True
    else:
        return False

def is_alphabet(uchar):
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    else:
        return False

if __name__ == '__main__':

    # filename = '../dataset/spider_result_1/result_2_addtype2.csv'
    filename = '../dataset/test_2/test_pre.csv'
    filename1 = '../dataset/test_2/test.csv'
    reader = pd.read_csv(filename, encoding='utf-8')
    reader1 = pd.read_csv(filename1, encoding='utf-8')
    unChinese = []
    specialwords = []
    count = 0
    blank = 0
    for string in reader['cuttedtext']:
        count += 1
        if str(string) == 'nan':
            tmp1 = reader['changedlabel'][count - 1]
            tmp2 = reader1['content'][count - 1]
            print("{}\t{}".format(tmp1,tmp2))
            specialwords.append("{}\t{}\n".format(tmp1,tmp2))
            continue
        for charitem in string:
            if not (is_chinese(charitem) or is_number(charitem) or is_alphabet(charitem)): unChinese.append(charitem + '\n')
        # print('处理完了第{}个文本'.format(count))

    unChinese = set(unChinese)

    f = open("../dataset/stopwords/filter2.txt", "a", encoding='utf-8')
    f.writelines(unChinese)
    f.close()

    f1 = open("../dataset/stopwords/specialwords2.txt", "a", encoding='utf-8')
    f1.writelines(specialwords)
    f1.close()