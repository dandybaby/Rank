import jieba.analyse
import logging
from textrank4zh import TextRank4Keyword, TextRank4Sentence
# 取消jieba 的日志输出
jieba.setLogLevel(logging.INFO)
# 读取文件
text = open('news.txt').read()
tags = jieba.analyse.textrank(text, topK=10, withWeight=True)
for tag in tags:
    print("关键词:%s\t\t weight:%f" % (tag[0], tag[1]))
# 输出重要的句子
tr4s = TextRank4Sentence()
tr4s.analyze(text=text, lower=True, source='all_filters')
print('摘要：')
# 重要性较高的三个句子
for item in tr4s.get_key_sentences(num=3):
    # index是语句在文本中位置，weight表示权重
    print(item.index, item.weight, item.sentence)
