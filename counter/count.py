import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image
import random

def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h, s, l = random.choice([(188, 72, 53), (253, 63, 56), (12, 78, 69)])#三个颜色的字体
    return "hsl({}, {}%, {}%)".format(h, s, l)

def till_word(train):
    tmp = []
    for item in train['text']:
        if str(item) == 'nan': tmp.append([''])
        else: tmp.append(item.split(' '))
    return tmp

if __name__ == '__main__':
    train1 = pd.read_csv('../dataset/test_1/train_pre.csv', header=None, names=['label', 'text'])
    train2 = pd.read_csv('../dataset/test_2/train_pre.csv', header=None, names=['label', 'text'])
    train3 = pd.read_csv('../dataset/test_3/train_pre.csv', header=None, names=['label', 'text'])
    tmp1 = till_word(train1)
    tmp2 = till_word(train2)
    tmp3 = till_word(train3)
    train_word_num1 = [len(text) for text in tmp1]
    train_word_num2 = [len(text) for text in tmp2]
    train_word_num3 = [len(text) for text in tmp3]
    train1['train_word_num'] = train_word_num1
    train2['train_word_num'] = train_word_num2
    train3['train_word_num'] = train_word_num3
    # plt.figure(figsize=(8,5))
    # _ = plt.hist(train_word_num3, bins = 100)
    # plt.xlabel('word number')
    # plt.ylabel('Freq')
    # plt.show()
    word_list = []
    for item in tmp1:
        word_list.append(' '.join(item))
    text = ' '.join(word_list)
    background_Image = np.array(Image.open('../images and fonts/2.jpg'))

    wc = WordCloud(
        background_color='white',
        mask=background_Image,
        font_path=r'../images and fonts/SourceHanSerifCN-Medium.otf',
        color_func=random_color_func,
        random_state=50,
        width=1800,
        height=2300
    )
    word_cloud = wc.generate(text)  # 产生词云
    word_cloud.to_file("../images and fonts/result1.jpg")  # 保存图片
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()
