import os
import pandas as pd

def count_Type(filepath):
    delete = 0
    right = 0
    close = 0
    other = 0
    file = pd.read_csv(filepath)
    for type in file['vote']:
        if type == 1: delete += 1
        elif type == 2: right += 1
        elif type == 4: close += 1
        else: other += 1
    return delete, right, close, other

def count_Diff_Dir():
    # Load all filedir.
    filedir = []
    for item in os.listdir():
        if (os.path.isdir(item) and '.' not in item and 'result' not in item and 'all' not in item):
            filedir.append(item)
    # Variables.
    count = 0
    delete = 0
    right = 0
    close = 0
    other = 0

    for files in filedir:
        for item in os.listdir(files):
            deleteadd = 0
            rightadd = 0
            closeadd = 0
            otheradd = 0

            count += 1
            print('处理了第{}个文件，文件名为{}'.format(count, item))
            deleteadd, rightadd, closeadd, otheradd = count_Type(files+'/'+item)
            delete += deleteadd
            right += rightadd
            close += closeadd
            other += otheradd

    return delete, right, close, other

def count_Diff_files(filepath):
    # Variables.
    count = 0
    delete = 0
    right = 0
    close = 0
    other = 0

    for item in os.listdir(filepath):
        if ('csv' in item):
            deleteadd = 0
            rightadd = 0
            closeadd = 0
            otheradd = 0

            count += 1
            print('处理了第{}个文件，文件名为{}'.format(count, item))
            deleteadd, rightadd, closeadd, otheradd = count_Type(filepath+'/'+item)
            delete += deleteadd
            right += rightadd
            close += closeadd
            other += otheradd

    return delete, right, close, other

def count_One_file(filepath):
    # Variables.
    delete = 0
    right = 0
    close = 0
    other = 0

    deleteadd = 0
    rightadd = 0
    closeadd = 0
    otheradd = 0

    print('处理文件名为{}'.format(filepath))
    deleteadd, rightadd, closeadd, otheradd = count_Type(filepath)
    delete += deleteadd
    right += rightadd
    close += closeadd
    other += otheradd

    return delete, right, close, other

if __name__ == "__main__":
    print('************文件统计程序************')
    print('**********************************')
    judge = input('输入1统计多个文件夹文件，输入2统计一个文件夹所有文件，输入3统计一个文件，输入0退出程序')
    while judge != '1' and judge != '2' and judge != '3' and judge != '0':
        judge = input('您的输入有误，请输入1统计多个文件夹文件，输入2统计一个文件夹所有文件，输入3统计一个文件，输入0退出程序')

    delete = 0
    right = 0
    close = 0
    other = 0

    if judge == '0':
        os._exit()
    if judge == '1':
        delete, right, close, other = count_Diff_Dir()
    if judge == '2':
        filepath = input('请输入文件夹路径') #filepath = '../dataset/spider_all'
        delete, right, close, other = count_Diff_files(filepath)
    if judge == '3':
        filename = '../dataset/model_data/b_pinglun_all.csv'# filename = input('请输入文件路径')
        delete, right, close, other = count_One_file(filename)

    print('得到全部文件的1类个数为{},2类的个数为{},4类的个数为{},其他的个数为{}'.format(delete, right, close, other))
