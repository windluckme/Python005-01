import requests
from time import sleep
import os
from lxml import etree
from pathlib import Path
import json
import sys

def get_answer(url):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    header = {'user-agent':ua}
    
    cookies={'cookie':'SESSIONID=DoHJK6qvKLECfI7S9uhc1zNGv2PARYwct6AEgg53c6M; JOID=UVgTC0LGESHBNS6sY824vzG6B-J05jQM4xwOiU7vMQTsFweMRsot4pU8K6RsORqoCVMUnWd6VkZ-xIydJJRHx28=; osd=UlAUA0PFGSbJNC2kZMW5vDm9D-N37jME4h8GjkbuMgzrHwaPTs0l45Y0LKxtOhKvAVIXlWByV0V2w4ScJ5xAz24=; _zap=8a6ccd27-2884-4454-84df-b2d279abc3f7; d_c0="ABAeHX4iRxKPTmHlJbbvZQ3yQb1hL3KopyE=|1606791416"; capsion_ticket="2|1:0|10:1606793408|14:capsion_ticket|44:Y2NmMGU2Mzg3ZTE3NDdhOWE0NjIyYjQwOTk1NzZjOTc=|8d3873b704b211c0fd4d087bd2195387ab2bcbd4bc34df4ed6104b04116896ac"; z_c0="2|1:0|10:1606793423|4:z_c0|92:Mi4xRlFuMUF3QUFBQUFBRUI0ZGZpSkhFaWNBQUFDRUFsVk56MFh0WHdDV3c2WVE2NW9oQjM5bkxQcTZuWDBrbWdJcHRn|71103543353a7f570836933b0a578199429ce0a5337ae75275d3e153fcb0d612"; _xsrf=42e16786-ff58-4169-80b7-77a6817eefbd; q_c1=08e57640faba446089b065ca77315cbe|1607218184000|1607218184000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1607138640,1607218182,1607241113,1607241303; tst=h; tshl=; KLBRSID=0a401b23e8a71b70de2f4b37f5b4e379|1607241761|1607241112; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1607241762'}
    
    try:
        response = requests.get(url,headers=header,cookies=cookies)
        print(1)
    except:
        print(2)
        sys.exit(1)
    
    selector = etree.HTML(response.text)

    answers = selector.xpath('//div[@class="RichContent RichContent--unescapable"]//span/p/text()')
    # print(answers)
    
    filename = 'answer.json' 
    with open(filename,'w') as file_obj:
        json.dump(answers,file_obj)

    
    
          

if __name__ == '__main__':
    myurl = 'https://www.zhihu.com/question/300985609'
    get_answer(myurl)
    

    


