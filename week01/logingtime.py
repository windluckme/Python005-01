import os
import logging
import time
import pathlib


def time_func():
    #获取当前时间日期
    today = time.strftime("%Y-%m-%d", time.localtime())
    hour = time.localtime().tm_hour
    
    #文件路径
    dirPath = os.getcwd() + "\var\log\python-" + today
    logfile = "logout.log"
    
    #判断当前路径是否存在
    if not os.path.exists(dirPath):
        # 不存在则创建
        os.makedirs(dirPath)
    #切换操作目录
    os.chdir(dirPath)
    
    #日志格式
    logging.basicConfig(filename='logfile',
                        level=logging,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format="%(asctime)s %(name)s [line: %(lineno)d] %(message)s)")
    logging.info('函数调用')
    
if __name__ == '__main__':
    print(time_func)