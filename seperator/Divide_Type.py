import csv

if __name__ == '__main__':
    f1 = open(r'../dataset/divide_type/1type_3.csv', 'w+', encoding='utf-8', newline='')
    f2 = open(r'../dataset/divide_type/2type_3.csv', 'w+', encoding='utf-8', newline='')
    f4 = open(r'../dataset/divide_type/4type_3.csv', 'w+', encoding='utf-8', newline='')

    fieldnames = ['opid', 'vote', 'content', 'cid']

    writer1 = csv.DictWriter(f1, fieldnames=fieldnames)
    writer1.writeheader()
    writer2 = csv.DictWriter(f2, fieldnames=fieldnames)
    writer2.writeheader()
    writer4 = csv.DictWriter(f4, fieldnames=fieldnames)
    writer4.writeheader()

    data = open(r'../dataset/spider_result_1/result_2_addtype2.csv', encoding='utf-8')

    reader = csv.reader(data)
    count = 0
    for row in reader:
        count += 1
        if count == 1: continue
        else:
            info = {
                'opid': row[0],
                'vote': row[1],
                'content': row[2],
                'cid': row[3],
            }
            if row[1] == '1': writer1.writerow(info)
            if row[1] == '2': writer2.writerow(info)
            if row[1] == '4': writer4.writerow(info)
            print("处理完了第{}行的数据".format(count))

    data.close()
    f1.close()
    f2.close()
    f4.close()

