import pandas as pd

if __name__ == '__main__':
    filename = input('请输入需要删除信息的文件名') #../dataset/spider_result_1/result_2_addtype2.csv, test:spider_6/695703-696300.csv
    reader = pd.read_csv(filename, encoding='utf-8')
    reader.drop(['cid'],axis=1,inplace=True)
    reader.drop(['opid'],axis=1,inplace=True)
    reader.to_csv('../dataset/dataset.csv', index = False)
    # print(reader)