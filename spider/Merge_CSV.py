import pandas as pd
import os

if __name__ == '__main__':
    filepath = '../dataset/spider_all'
    filelist = os.listdir(filepath)
    filelist.sort(key=lambda x: int(x.split("-")[0]))
    file = []
    count = 0
    for f in filelist:
        count += 1
        filename = filepath + '/' + f
        print('处理了第{}个文件，文件名为{}'.format(count, filename))
        file.append(pd.read_csv(filename))
    fresult = pd.concat(file)
    fresult.to_csv("../dataset/spider_result_1/result_2_addtype2" + ".csv", index=0, sep=',')

