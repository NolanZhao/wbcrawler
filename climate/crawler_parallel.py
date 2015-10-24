# !/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created on Oct 16, 2015
# @author:       Bo Zhao
# @email:        bo_zhao@hks.harvard.edu
# @website:      http://yenching.org
# @organization: Harvard Kennedy School

import sys

sys.path.append("/home/bo/.local/lib/python2.7/site-packages")
sys.path.append("/home/bo/Workspace/wbcrawler")
sys.path.append("/home/bo/Workspace/wbcrawler/climate")

# libraries
from settings import project, address, port, Rbt_NUM
from wbcrawler.parallel import parallel_crawling
from wbcrawler.database import unlock_robots

# repost, path, info = 2, 0, 0

# funcs
parallel_crawling(Rbt_NUM, 0, 0, project, address, port)
unlock_robots('local', address, port)
parallel_crawling(0, Rbt_NUM, 0, project, address, port)
unlock_robots('local', address, port)
parallel_crawling(0, 0, Rbt_NUM, project, address, port)
unlock_robots('local', address, port)

if __name__ == '__main__':
    pass
