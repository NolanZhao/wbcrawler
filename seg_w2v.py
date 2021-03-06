# !/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created on Oct 16, 2015
# @author:       Bo Zhao
# @email:        bo_zhao@hks.harvard.edu
# @website:      http://yenching.org
# @organization: Harvard Kennedy School

import sys
from pymongo import MongoClient
from wbcrawler.log import *
from wbcrawler.seg import seg_sentence
from gensim.models import Word2Vec

reload(sys)
sys.setdefaultencoding('utf-8')

address = "localhost"
port = 27017
project = 'insurance'

# words = []
# sentences = []
# client = MongoClient(address, port)
# db = client[project]
# posts = db.posts.find()
# log(NOTICE, "total posts %d" % posts.count())
#
# i = 0
# for post in posts:
#     sentence = seg_sentence(post['content'])
#     words.extend(sentence.split(u' '))
#     sentences.append(sentence.split(u' '))
#     i += 1
#     log(NOTICE, "post # %d" % i)
#
# model = Word2Vec(sentences, min_count=5, workers=10)
#
# model.save('%s/w2v.bin' % project)
# log(NOTICE, 'mission completes')

model = Word2Vec.load('%s/w2v.bin' % project)
for w, i in model.most_similar([u'商业保险'], topn=1000):
    # log(NOTICE, w + ' ' + str(i))
    print w.encode('gbk', 'ignore') + ' ' + str(i).encode('gbk', 'ignore')


# print '================'
for w, i in model.most_similar(positive=[u'保险'], negative=[u'社会保险', u'社保'], topn=10):
    log(NOTICE, w + ' ' + str(i))
#
# print '================'
print model.similarity(u'商保', u'社保')
print model.similarity(u'商保', u'社会保险')
# print model.similarity(u'官员', u'官员')
# print model.similarity(u'官员', u'人民')
# pass
# print '================'
# print model[u'政府']
