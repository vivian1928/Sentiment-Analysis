import requests
import re
import json
import csv
import os
from shutil import copy
from urllib import request

# Headers.
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
# Control max id and cid.
id_Max = '1288800'
cid_Max = ['1495','38032','74569','111106','147643','184180','220717','257254','293791','330328',
           '366865','403402','439939','476476','513013','549550','586087','622624','659161','695698',
           '732235','768772','805309','841846','878383','914920','951457','987994','1024531','1061068',
           '1097605','1134142','1170679','1207216','1243753','1280290','1316827','1353364','1389901','1426438',
           '1462975','1499512','1535640']
cid_Min = ['1068','37605','74142','110679','147216','183753','220290','256827','293364','329901',
           '366438','402975','439512','476049','512586','549123','585660','622197','658734','695271',
           '731808','768345','804882','841419','877956','914493','951030','987567','1024104','1060641',
           '1097178','1133715','1170252','1206789','1243326','1279863','1316400','1352937','1389474','1426011',
           '1462548','1499085','1535622']
# Save in csv files.
def save_csv(filename, info):
    with open(filename, 'a', encoding='utf-8', newline="") as f:
        if 'main' in filename: fieldnames = ['id', 'cid', 'originContentModify', 'punishType', 'punishTypeName', 'reasonType', 'reasonTypeName']
        if 'opinion' in filename: fieldnames = ['opid', 'vote', 'content', 'cid']
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writerow(info)

# Connect html page and get text.
def get_html_text(judge):
    # Scanned id and case id.
    cid = 1503568#int(cid_Max[41]) #- 1 #min cid each time download needed to edit
    id = 0
    cidmax = int(cid_Min[42]) #max cid each time download needed to edit
    # Api for main and opinion blackroom pages.
    if judge == 'main':
        while id < int(id_Max):
            id += 1
            url_main = 'https://api.bilibili.com/x/credit/blocked/info?jsonp=jsonp&id={}'.format(id)
            html = requests.get(url_main, headers = headers)
            dicts = json.loads(html.content)
            if (dicts['code'] == -404):
                print('该id没有内容'.format(id))
                continue
            get_main_info(dicts['data'])
            print('当前爬取的id{}'.format(id))

    if judge == 'opinion':
        while cid < cidmax:
            cid += 1
            page_index = 0
            # flag = False # judge None
            while True:
                page_index += 1
                url_opinion = 'https://api.bilibili.com/x/credit/jury/case/opinion?jsonp=jsonp&cid={}&pn={}&ps=10'.format(
                    cid,
                    page_index)
                html = requests.get(url_opinion, headers = headers)
                dicts = json.loads(html.content)
                if (dicts['data']['opinion'] == None or page_index > 1):
                    break
                get_opinion_info(cid, dicts['data']['opinion'])
            print('当前爬取的案例{}'.format(cid))

# Process main page data, extract originContentModify, punishType, punishTypeName, reasonType, reasonTypeName, caseId
def get_main_info(data):
    for i in data:
        Tmp = i['originContentModify']
        Tmp = ((str(Tmp).replace("'", '"')).replace('True', 'true')).replace('False', 'false')
        re_h = re.compile('</?\w+[^>]*>')
        Tmp = re_h.sub('', Tmp)
        originContentModify, sep, tail = Tmp.partition('批注')
        #originContentModify = Tmp.replace('(?<批注).*','')
        punishType = i['punishType']
        punishTypeName = i['punishTypeName']
        reasonType = i['reasonType']
        reasonTypeName = i['reasonTypeName']
        caseId = i['caseId']
        id = i['id']
        info = {
            'id': id,
            'cid': caseId,
            'originContentModify': originContentModify,
            'punishType': punishType,
            'punishTypeName': punishTypeName,
            'reasonType': reasonType,
            'reasonTypeName': reasonTypeName
        }
        filename = 'main.csv'
        save_csv(filename, info)

# Process opinion page opinion, extract vote, content, opid
def get_opinion_info(cid, opinion):
    for i in opinion:
        vote = i['vote']
        content = i['content'].replace('\n', '').replace('\r', '').replace( "\'", "" ).replace( "\"", "" )
        opid = i['opid']
        info = {
            'cid': cid,
            'opid': opid,
            'vote': vote,
            'content': content
        }
        filename = 'opinion.csv'
        save_csv(filename, info)

if __name__ == '__main__':
    filename = 'loading/main.csv'
    with open(filename, 'w', encoding='utf-8', newline="") as f:
        fieldnames = ['id', 'cid', 'originContentModify', 'punishType', 'punishTypeName', 'reasonType',
                                             'reasonTypeName']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
    filename = 'loading/opinion.csv'
    with open(filename, 'w', encoding='utf-8', newline="") as f:
        fieldnames = ['opid', 'vote', 'content', 'cid']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
    print('************bilibili小黑屋爬虫************')
    print('****************************************')
    judge = input('输入main爬取主界面信息，输入opinion爬取评论界面信息')
    while judge != 'main' and judge != 'opinion':
        judge = input('您的输入有误，请输入main爬取主界面信息，输入opinion爬取评论界面信息，输入0结束程序')
        if judge == '0':
            os._exit()
    get_html_text(judge)
    save_path = 'C:\\Users\\Vivian Meng\\PycharmProjects\\Bilibili_Blackroom_Spider\\dataset\\spider_3' + cid_Max[41] + '-' + cid_Min[42] + '.csv' #save path each time download needed to edit
    copy('C:\\Users\\Vivian Meng\\PycharmProjects\\Bilibili_Blackroom_Spider\\dataset\\loading\\opinion.csv', save_path)