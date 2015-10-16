# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Oct 14, 2015
@author:       Bo Zhao
@email:        bo_zhao@hks.harvard.edu
@website:      http://yenching.org
@organization: Harvard University
'''

import sys

from snownlp import SnowNLP as sn

reload(sys)
sys.setdefaultencoding('utf-8')

s = sn(u"这个东西真赞")
for w in s.words:
    print w.decode('utf-8')
print s.tags
print s.sentiments

text = u'''
自然语言处理是计算机科学领域与人工智能领域中的一个重要方向。
它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。
自然语言处理是一门融语言学、计算机科学、数学于一体的科学。
因此，这一领域的研究将涉及自然语言，即人们日常使用的语言，
所以它与语言学的研究有着密切的联系，但又有重要的区别。
自然语言处理并不是一般地研究自然语言，
而在于研制能有效地实现自然语言通信的计算机系统，
特别是其中的软件系统。因而它是计算机科学的一部分。
'''

s2 = sn(text)
print s2.sentiments
