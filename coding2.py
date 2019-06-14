#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Hein Htet Aung
# @Date:   2019-06-14 12:34:34
# @Last Modified by:   Hein Htet Aung
# @Last Modified time: 2019-06-14 12:49:48
import requests,re
pattern = re.compile('<\s*textarea[^>]*>([^<]*)<\s*\/\s*textarea\s*>',re.IGNORECASE)
customcookie = {'PHPSESSID':'Your cookie Here'}
url = 'https://www.hackthis.co.uk/levels/coding/2'
r = requests.get(url,cookies=customcookie)
hexs = re.findall(pattern,r.text)
hexlist = hexs[0].encode('utf-8').split(',')
flag = ""
for i in hexlist:
	if i!=' ':
		flag = flag + unichr(126-int(i))
	else:
		flag = flag + i
flag = flag.lower()
r2 = requests.post(url,data={'answer':flag},cookies=customcookie)
print flag
