# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ipset=input("Please type IP(like: 10.1.1.0/24)")
print(ipset)
ip = ipset[:-3].split('.')
mask1 = int(ipset[-2:])
mask0 = 32-mask1
maskb =int(mask1 * "1" + mask0 * "0")
templateip = '''
{:<8} {:<8} {:<8} {:<8}
'''

templateb = '''
{:<08b} {:<08b} {:<08b} {:<08b}
'''
print("Network:")
print(templateip.format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3])))
print(templateb.format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3])))

print("Mask:")
print("/", mask1)
print(maskb)
#print(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3]))