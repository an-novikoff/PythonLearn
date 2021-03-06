# -*- coding: utf-8 -*-
'''
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
command1 = command1.split()
command2 = command2.split()
vlans1 = command1[-1].split(',')
vlans2 = command2[-1].split(',')
set1 = set(vlans1)
set2 = set(vlans2)
set_all = set1 & set2
print(sorted(set_all))
