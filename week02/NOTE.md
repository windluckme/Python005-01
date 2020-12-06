# 学习笔记
OSI7层参考模型 ICP/IP模型
根据定位的层级，解决相应的问题

## 基于TCP的Socket编程/通信模型
Socket API
socket()
bind()
listen()
accept()
recv()
send()
close()
### [socket TCP编程](https://gitee.com/windluckme/pythontrain/blob/master/version_2.0/week2/mod2_client2.py)
AF_INET 表示IPv4地址 SOCK_STREAM 表示TCP协议
# buffer = []
# while True: 建立一个死循环   
#    data = s.recv(1024)   recv接收服务器返回的内容 接收多少字符（1024）
#    if data:			如果接受的是非空的
#        buffer.append(data)   存入到fuffer
#    else:	
#        break	

###[http协议编程](https://gitee.com/windluckme/pythontrain/blob/master/version_2.0/week2/mod2_client1.py)


## echo server 回显
echo服务器检查微服务
[Echo Server 的 Client 客户端](https://gitee.com/windluckme/pythontrain/blob/master/version_2.0/week2/mod2_echo_client.py)
.decode('utf-8')解码 windows上GBK
[Echo Server 的 Server 服务端](https://gitee.com/windluckme/pythontrain/blob/master/version_2.0/week2/mod2_echo_server.py)
.bind 绑定

get会在地址栏显示出来 请求数据会附在URL上 ?分割URL和传输数据 &多个参数连接
	由于浏览器地址栏长度限制传输数据有限
post会把数据放置在HTTP包的包体中 数据栏不会改变 更加安全
	不会导致传输数据限制 一般用于用户和密码的登录

## HTML标签
span 文本
	span（文本）：用于包裹一部分文字，进行特定样式的修改。
	<span style="color:red; font-size:36px;">酷</span>！！
img 图片
a 超链接
em 强调
strong 强调
q 短引用
i 倾斜
b 加粗
u 下划线

with open 上下文管理器
捕获异常从下往上看 
Exception 捕获所有的异常

## 编程规范
PEP-8
Google python 风格指引

## 自顶向下
分析需求，拆分需求，将拆分的需求模块化，将模块化内容填充完整

## scrapy框架图 爬虫
engine 引擎： 多线程和协程 各个组件的中间调度
spiders 爬虫：预处理 将爬虫概念实例化 
scheduler 调度器： 确定发起顺序 范围 并发控制
download 下载器： 模拟浏览器发起请求 保存
itemPipeline 管道 : 进行后期处理（详细分析、过滤、存储等）








