#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Hein Htet Aung
# @Date:   2019-06-14 09:48:54
# @Last Modified by:   Hein Htet Aung
# @Last Modified time: 2019-06-14 11:04:56
import re,requests
pattern = re.compile('<\s*textarea[^>]*>([^<]*)<\s*\/\s*textarea\s*>',re.IGNORECASE)
url = 'https://www.hackthis.co.uk/levels/coding/1'
customcookie = {'PHPSESSID':'cnuiisl0q3g8ev0gbvdal5ojr1; _ga=GA1.3.1612931587.1560480664; _gid=GA1.3.1050919009.1560480664; member=1; autologin=8%97%CAm%E7s%FE%98%E0%A0t%C3U%A1I%D5%86%BB%FE%E0%81+E%8B%60%8F%7F%02%8E%9D%F2%3Eh%E3N%E5%16%8EL%06Y%98%24%99%AB%0E%8C%C9%E7%CE%2B%E5%19%F5v%0FE%C8%A6k%B0%7D%EB%B2; _gat=1'}
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