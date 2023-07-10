import csv
import random
import numpy as np
import pandas as pd



# Choose randomly for each type of ratio 31000:3000:6000 and sum of data is 120000.
def third_test_choose(type1, type2, type4):
    random_list_1 = random.sample(range(0, len(type1)), 40000)
    random_list_2 = random.sample(range(0, len(type2)), 40000)
    random_list_4 = random.sample(range(0, len(type4)), 40000)
    random_strlist_1 = ['a' + str(i) for i in random_list_1]
    random_strlist_2 = ['b' + str(i) for i in random_list_2]
    random_strlist_4 = ['c' + str(i) for i in random_list_4]

    list_93000 = []
    list_9000 = []
    list_18000 = []

    list_93000[:31000] = random_strlist_1[:31000]
    list_93000[31000:62000] = random_strlist_2[:31000]
    list_93000[62000:93000] = random_strlist_4[:31000]

    list_9000[:3000] = random_strlist_1[31000:34000]
    list_9000[3000:6000] = random_strlist_2[31000:34000]
    list_9000[6000:9000] = random_strlist_4[31000:34000]

    list_18000[:6000] = random_strlist_1[34000:40000]
    list_18000[6000:12000] = random_strlist_2[34000:40000]
    list_18000[12000:18000] = random_strlist_4[34000:40000]

    random.shuffle(list_93000)
    random.shuffle(list_9000)
    random.shuffle(list_18000)

    train_list = []
    val_list = []
    test_list = []

    for item in list_93000:
        if item[0] == 'a': train_list.append(type1[int(item[1:])])
        if item[0] == 'b': train_list.append(type2[int(item[1:])])
        if item[0] == 'c': train_list.append(type4[int(item[1:])])

    for item in list_9000:
        if item[0] == 'a': val_list.append(type1[int(item[1:])])
        if item[0] == 'b': val_list.append(type2[int(item[1:])])
        if item[0] == 'c': val_list.append(type4[int(item[1:])])

    for item in list_18000:
        if item[0] == 'a': test_list.append(type1[int(item[1:])])
        if item[0] == 'b': test_list.append(type2[int(item[1:])])
        if item[0] == 'c': test_list.append(type4[int(item[1:])])

    fieldnames = ['opid', 'vote', 'content', 'cid']

    train_dict_list = []
    for data in train_list:
        train_dict = dict.fromkeys(('opid', 'vote', 'content', 'cid'))
        data = data.replace('\n', '').replace('\r', '')
        tmp = data.split(',')
        train_dict.update({'opid': tmp[0], 'vote': tmp[1], 'content': tmp[2], 'cid': tmp[3]})
        train_dict_list.append(train_dict)

    val_dict_list = []
    for data in val_list:
        val_dict = dict.fromkeys(('opid', 'vote', 'content', 'cid'))
        data = data.replace('\n', '').replace('\r', '')
        tmp = data.split(',')
        val_dict.update({'opid': tmp[0], 'vote': tmp[1], 'content': tmp[2], 'cid': tmp[3]})
        val_dict_list.append(val_dict)

    test_dict_list = []
    for data in test_list:
        test_dict = dict.fromkeys(('opid', 'vote', 'content', 'cid'))
        data = data.replace('\n', '').replace('\r', '')
        tmp = data.split(',')
        test_dict.update({'opid': tmp[0], 'vote': tmp[1], 'content': tmp[2], 'cid': tmp[3]})
        test_dict_list.append(test_dict)

    writer1 = pd.DataFrame(columns=fieldnames, data=train_dict_list)
    writer1.to_csv('../dataset/spider_result_1/train_3.csv', encoding='utf-8', index=False)

    writer2 = pd.DataFrame(columns=fieldnames, data=val_dict_list)
    writer2.to_csv('../dataset/spider_result_1/val_3.csv', encoding='utf-8', index=False)

    writer4 = pd.DataFrame(columns=fieldnames, data=test_dict_list)
    writer4.to_csv('../dataset/spider_result_1/test_3.csv', encoding='utf-8', index=False)


# Choose randomly for each type of ratio 20000:2000:4000 and sum of data is 78000.
def second_test_choose(type1, type2, type4):
    random_list_1 = random.sample(range(0, len(type1)), 26000)
    random_list_2 = random.sample(range(0, len(type2)), 26000)
    random_list_4 = random.sample(range(0, len(type4)), 26000)
    random_strlist_1 = ['a' + str(i) for i in random_list_1]
    random_strlist_2 = ['b' + str(i) for i in random_list_2]
    random_strlist_4 = ['c' + str(i) for i in random_list_4]

    list_60000 = []
    list_6000 = []
    list_12000 = []

    list_60000[:20000] = random_strlist_1[:20000]
    list_60000[20000:40000] = random_strlist_2[:20000]
    list_60000[40000:60000] = random_strlist_4[:20000]

    list_6000[:2000] = random_strlist_1[20000:22000]
    list_6000[2000:4000] = random_strlist_2[20000:22000]
    list_6000[4000:6000] = random_strlist_4[20000:22000]

    list_12000[:4000] = random_strlist_1[22000:26000]
    list_12000[4000:8000] = random_strlist_2[22000:26000]
    list_12000[8000:12000] = random_strlist_4[22000:26000]

    random.shuffle(list_60000)
    random.shuffle(list_6000)
    random.shuffle(list_12000)

    train_list = []
    val_list = []
    test_list = []

    for item in list_60000:
        if item[0] == 'a': train_list.append(type1[int(item[1:])])
        if item[0] == 'b': train_list.append(type2[int(item[1:])])
        if item[0] == 'c': train_list.append(type4[int(item[1:])])

    for item in list_6000:
        if item[0] == 'a': val_list.append(type1[int(item[1:])])
        if item[0] == 'b': val_list.append(type2[int(item[1:])])
        if item[0] == 'c': val_list.append(type4[int(item[1:])])

    for item in list_12000:
        if item[0] == 'a': test_list.append(type1[int(item[1:])])
        if item[0] == 'b': test_list.append(type2[int(item[1:])])
        if item[0] == 'c': test_list.append(type4[int(item[1:])])

    fieldnames = ['opid', 'vote', 'content', 'cid']

    train_dict_list = []
    for data in train_list:
        train_dict = dict.fromkeys(('opid', 'vote', 'content', 'cid'))
        data = data.replace('\n', '').replace('\r', '')
        tmp = data.split(',')
        train_dict.update({'opid': tmp[0], 'vote': tmp[1], 'content': tmp[2], 'cid': tmp[3]})
        train_dict_list.append(train_dict)

    val_dict_list = []
    for data in val_list:
        val_dict = dict.fromkeys(('opid', 'vote', 'content', 'cid'))
        data = data.replace('\n', '').replace('\r', '')
        tmp = data.split(',')
        val_dict.update({'opid': tmp[0], 'vote': tmp[1], 'content': tmp[2], 'cid': tmp[3]})
        val_dict_list.append(val_dict)

    test_dict_list = []
    for data in test_list:
        test_dict = dict.fromkeys(('opid', 'vote', 'content', 'cid'))
        data = data.replace('\n', '').replace('\r', '')
        tmp = data.split(',')
        test_dict.update({'opid': tmp[0], 'vote': tmp[1], 'content': tmp[2], 'cid': tmp[3]})
        test_dict_list.append(test_dict)

    writer1 = pd.DataFrame(columns=fieldnames, data=train_dict_list)
    writer1.to_csv('../dataset/spider_result_1/train_2.csv', encoding='utf-8', index=False)

    writer2 = pd.DataFrame(columns=fieldnames, data=val_dict_list)
    writer2.to_csv('../dataset/spider_result_1/val_2.csv', encoding='utf-8', index=False)

    writer4 = pd.DataFrame(columns=fieldnames, data=test_dict_list)
    writer4.to_csv('../dataset/spider_result_1/test_2.csv', encoding='utf-8', index=False)


# Choose randomly for each type of ratio 2000:200:400 and sum of data is 7800.
def first_test_choose(type1, type2, type4):
    random_list_1 = random.sample(range(0, len(type1)), 2600)
    random_list_2 = random.sample(range(0, len(type2)), 2600)
    random_list_4 = random.sample(range(0, len(type4)), 2600)
    random_strlist_1 = ['a' + str(i) for i in random_list_1]
    random_strlist_2 = ['b' + str(i) for i in random_list_2]
    random_strlist_4 = ['c' + str(i) for i in random_list_4]

    list_6000 = []
    list_600 = []
    list_1200 = []

    list_6000[:2000] = random_strlist_1[:2000]
    list_6000[2000:4000] = random_strlist_2[:2000]
    list_6000[4000:6000] = random_strlist_4[:2000]

    list_600[:200] = random_strlist_1[2000:2200]
    list_600[200:400] = random_strlist_2[2000:2200]
    list_600[400:600] = random_strlist_4[2000:2200]

    list_1200[:400] = random_strlist_1[2200:2600]
    list_1200[400:8000] = random_strlist_2[2200:2600]
    list_1200[800:1200] = random_strlist_4[2200:2600]

    random.shuffle(list_6000)
    random.shuffle(list_600)
    random.shuffle(list_1200)

    train_list = []
    val_list = []
    test_list = []

    for item in list_6000:
        if item[0] == 'a': train_list.append(type1[int(item[1:])])
        if item[0] == 'b': train_list.append(type2[int(item[1:])])
        if item[0] == 'c': train_list.append(type4[int(item[1:])])

    for item in list_600:
        if item[0] == 'a': val_list.append(type1[int(item[1:])])
        if item[0] == 'b': val_list.append(type2[int(item[1:])])
        if item[0] == 'c': val_list.append(type4[int(item[1:])])

    for item in list_1200:
        if item[0] == 'a': test_list.append(type1[int(item[1:])])
        if item[0] == 'b': test_list.append(type2[int(item[1:])])
        if item[0] == 'c': test_list.append(type4[int(item[1:])])

    fieldnames = ['opid', 'vote', 'content', 'cid']

    train_dict_list = []
    for data in train_list:
        train_dict = dict.fromkeys(('opid', 'vote', 'content', 'cid'))
        data = data.replace('\n', '').replace('\r', '')
        tmp = data.split(',')
        train_dict.update({'opid': tmp[0], 'vote': tmp[1], 'content': tmp[2], 'cid': tmp[3]})
        train_dict_list.append(train_dict)

    val_dict_list = []
    for data in val_list:
        val_dict = dict.fromkeys(('opid', 'vote', 'content', 'cid'))
        data = data.replace('\n', '').replace('\r', '')
        tmp = data.split(',')
        val_dict.update({'opid': tmp[0], 'vote': tmp[1], 'content': tmp[2], 'cid': tmp[3]})
        val_dict_list.append(val_dict)

    test_dict_list = []
    for data in test_list:
        test_dict = dict.fromkeys(('opid', 'vote', 'content', 'cid'))
        data = data.replace('\n', '').replace('\r', '')
        tmp = data.split(',')
        test_dict.update({'opid': tmp[0], 'vote': tmp[1], 'content': tmp[2], 'cid': tmp[3]})
        test_dict_list.append(test_dict)

    writer1 = pd.DataFrame(columns=fieldnames, data=train_dict_list)
    writer1.to_csv('../dataset/spider_result_1/train_1.csv', encoding='utf-8', index=False)

    writer2 = pd.DataFrame(columns=fieldnames, data=val_dict_list)
    writer2.to_csv('../dataset/spider_result_1/val_1.csv', encoding='utf-8', index=False)

    writer4 = pd.DataFrame(columns=fieldnames, data=test_dict_list)
    writer4.to_csv('../dataset/spider_result_1/test_1.csv', encoding='utf-8', index=False)


if __name__ == '__main__':
    filename1 = '../dataset/divide_type/1type_3.csv'
    filename2 = '../dataset/divide_type/2type_3.csv'
    filename4 = '../dataset/divide_type/4type_3.csv'
    type1 = open(filename1, encoding='utf-8').readlines()
    type2 = open(filename2, encoding='utf-8').readlines()
    type4 = open(filename4, encoding='utf-8').readlines()
    del type1[0]
    del type2[0]
    del type4[0]
    third_test_choose(type1, type2, type4)
