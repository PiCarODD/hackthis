#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Hein Htet Aung
# @Date:   2019-06-14 09:48:54
# @Last Modified by:   Hein Htet Aung
# @Last Modified time: 2019-06-14 11:04:56
import re,requests
pattern = re.compile('<\s*textarea[^>]*>([^<]*)<\s*\/\s*textarea\s*>',re.IGNORECASE)
url = 'https://www.hackthis.co.uk/levels/coding/1'
customcookie = {'PHPSESSID':'your cookies here'}
r = requests.get(url,cookies=customcookie)
data = re.findall(pattern,r.text)
splitdata = data[0].encode('utf-8').split(',')
splitdata[0] = " " + splitdata[0]
sortstr = sorted(splitdata)
sortstr[0] = sortstr[0].split(' ')[1]
flag = ','
flag = flag.join(sortstr)
r2 = requests.post(url,data={'answer':flag},cookies=customcookie)
print flag
