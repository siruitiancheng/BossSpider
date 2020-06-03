import os
import sys

from spider_boss import JobSpider

sys.path.append(os.path.abspath(__file__))

if __name__ == '__main__':
    job_spider = JobSpider()
    job_spider.run()