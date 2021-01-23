#-*- coding:utf-8 -*-

import requests
import json
import time

class define:
    GREEN       = "\033[32m"
    RED         = "\033[0;31m"
    BLUE        = "\033[94m"
    ORANGE      = "\033[33m"
    host        = "https://10.20.28.101:3443/"     #端口后面一定要加/
    api_key     = "1986ad8c0a5b3df4d7028d5f3c06e936c165b8a2c063541efac24e36f7c753686"                            #替换此处apikey
    api_header  = {'X-Auth':api_key,'content-type':'application/json'}
    filename    = 'out/%s.xlsx' % time.strftime("%Y-%m-%d-%H-%M", time.localtime(time.time()))
    awvs_scan_rule = {
                "full": "11111111-1111-1111-1111-111111111111",
                "highrisk": "11111111-1111-1111-1111-111111111112",
                "XSS": "11111111-1111-1111-1111-111111111116",
                "SQL": "11111111-1111-1111-1111-111111111113",
                "Weakpass": "11111111-1111-1111-1111-111111111115",
                "crawlonly": "11111111-1111-1111-1111-111111111117"
                    }
    banner = '''
                             
\__  |   |   |  |__   _____|__|_  _  __ ____ |__|
 /   |   |   |  |  \ /  ___/  \ \/ \/ // __ \|  |
 \____   |   |   Y  \\___ \|  |\     /\  ___/|  |
 / ______|___|___|  /____  >__| \/\_/  \___  >__|
 \/               \/     \/                \/   
                 

    [*] Author:请您尊重版权不要更改作者谢谢---Yihsiwei---高级渗透测试工程师
	[*] 请将awvs设置为每页100个
    '''
l = 100   
if __name__ == '__main__':
	print(define.ORANGE+define.banner)
	str1 = input("请输入准备导出多少个(小于等于100):")
	page = input("请输入您准备导出目标页中第几页的:")
	cpage = (int(page)-1)*100
	time.sleep(8)
	result = requests.get(define.host+"api/v1/targets?c="+str(cpage)+"&l="+str(l)+"&s=status:asc",headers=define.api_header,timeout=30,verify=False)
	results = json.loads(result.content)
	loopnum = int(str1)
	if results:
		for s in results["targets"]:
			if loopnum>0:
				target_id = s['target_id']
				data = {
				"template_id":"11111111-1111-1111-1111-111111111115",
				"source":{
					"list_type":"targets",
					"id_list":[target_id]
					}
				}
				requests.post(define.host+"api/v1/reports",headers=define.api_header,json=data,timeout=30,verify=False)
				print(target_id+"已导出\n")
				loopnum = loopnum - 1
			

	else :
		print("参数错误  如apikey 还有你的脑子")
	
	str = input("第"+page+"页已完成回车就可以退出")