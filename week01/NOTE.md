学习笔记

mkdir 新建目录
cd       进入目录
ls -al  查看内容
git init 初始化
git config --global user.name " "
git config --global user.email ""
git config --global --list
clear 清空屏幕

git status 状态
pwd 查看位置

git add +文件名去跟踪这个文件     .跟踪所有文件
git commit 提交 -m "creat learn_git.html" 注释版本说明

git log 显示历史的所有的提交

ssh-keygen -t rsa -C ""配置公司钥
cat 查看

git clone 克隆仓库


python -m venv venv1 创建虚拟环境
deactivate 退出虚拟环境

时间的访问和转换
import time

time.time()

time.localtime()

time.strftime(%Y-%m-%d %X, time.localtime())

time.strptime("2020-11-26 16:59:15", %Y-%m-%d %X)

基本的日期和时间类型
import datrtime

datetime.datetime.today()
form datetime import *  #等价

datetime.today()
datetime.now()

datetime.today() - timedelta(days=1)
datetime.today() + timedelta(days=-1)

日志级别
info
warning
error
debug
critical
import logging                                                                                                                                                           

logging.debug('This is debug message')                                                                                                                                   

logging.info('This is info message')                                                                                                                                     

logging.warning('This is warning message')                                                                                                                               
	WARNING:root:This is warning message

logging.error('This is error message')                                                                                                                                   
	ERROR:root:This is error message

logging.critical('This is critical message')                                                                                                                             
	CRITICAL:root:This is critical message
	
生成伪随机数

from random import *

randrange(0, 101, 2)  重成随机偶数                                                    

randrange(0, 101)   生成0-100 的随机数                                              

randrange(0, 101, 2)  生成0-100的随机偶数                                            

random() 生成0.0到1.0的随机伪浮点数（跟据当前时间戳）                                

choice(["red", "blue", "orange"])                                                      
'orange'

JSON 编码和解码

import json
    
json.loads('["foo", {"bar": ["baz", null, 1.8, 2]}]')       # json.loads 解码                      
['foo', {'bar': ['baz', None, 1.8, 2]}]

json.dumps("['foo', {'bar': ['baz', None, 1.8, 2]}]")       # json.dumps 编码                  
'"[\'foo\', {\'bar\': [\'baz\', None, 1.8, 2]}]"'

常见路径操作

import os                                                              

os.path.abspath('text.log')               # 获取给定文件的完整路径                            
'/user/text.log'

path = "/user/a.txt"                                     

os.path.basename(path)                     # 获取给定文件路径的文件名                 
'a.txt'

os.path.dirname(path)                      # 获取给定文件路径的路径      
'/user/local'

os.path.exists('/etc/hosts')               # 判断文件或目录是否存在        
True

os.path.isfile('/etc/hosts')                # 判断给定路径是否为目录                
True

os.path.join("a", "b")                      # 拼接路径       
'a/b' 
