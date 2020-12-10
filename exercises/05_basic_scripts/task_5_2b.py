# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv
#ipset=input("Please type IP(like: 10.1.1.0/24)")
ipset = argv[1]
print(ipset)
ip, mask = ipset.split('/')
ip = ip.split('.')
mask0 = 32-int(mask)
maskb =int(mask) * "1" + mask0 * "0"
m1,m2,m3,m4  = [int(maskb[0:8],2),int(maskb[8:16],2),int(maskb[16:24],2),int(maskb[24:33],2),]

templateip = '''
{:<8} {:<8} {:<8} {:<8}
'''

templateb = '''
{:<08b} {:<08b} {:<08b} {:<08b}
'''
print("Network:")
print(templateip.format(int(ip[0]),int(ip[1]),int(ip[2]),int(0)))
print(templateb.format(int(ip[0]),int(ip[1]),int(ip[2]),int(0)))

print("Mask:")
print("/", mask)
print(m1,m2,m3,m4)
print(templateb.format(m1,m2,m3,m4))
