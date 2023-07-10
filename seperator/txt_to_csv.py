import csv

if __name__ == '__main__':
    f = open(r'../dataset/model_data/b_pinglun_all.csv', 'w+', encoding='utf-8', newline='')
    writer = csv.writer(f)
    writer.writerow(['vote','content'])
    data = open(r'../dataset/model_data/b_pinglun_all.txt', encoding='utf-8')
    res = []
    for i in data:
        d = [x for x in i.strip().split('\t')]
        res.append(d)
    writer.writerows(res)
    data.close()
    f.close()
