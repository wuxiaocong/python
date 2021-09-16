import cfscrape
import time
import json
import re
scraper = cfscrape.create_scraper()
def check_json(input_str):
    try:
        json.loads(input_str)
        return True
    except:
        return False
i = 1
old_data = 'Please only have one black friday page open at any given time, and if you are on a third party website ensure that you are not having it refreshed too often in the background'
while (i < 2):
    time.sleep(1)
    web_data = scraper.get("https://billing.virmach.com/modules/addons/blackfriday/new_plan.json").content
    if(web_data != old_data):
        if check_json(web_data):
            old_data = web_data
            data = json.loads(web_data)
            if(data['windows'] == 'FALSE'):
                windows = '不支持WINDOWS'
            else:
                windows = '支持WINDOWS'
            if('ended' in data):
                print('当前秒杀已售罄')
            else:
                print('价格：$'+''.join(re.findall(r"\d+\.?\d*",data['price'])),'内存：',data['ram'],'核心：',data['cpu'],'IP：',data['ips'],'硬盘：',data['hdd'],'流量：',data['bw'],'地区：',data['location'],windows)
                print ('购买链接：https://billing.virmach.com/cart.php?a=add&pid=' + str(data['pid']) + '&billingcycle=annually')
