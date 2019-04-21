
from scrapy.cmdline import execute

import sys
import os

print(os.path.dirname(os.path.abspath(__file__)))

'''本地调试需要黄建main.py文件'''

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","rengongzhineng"])
