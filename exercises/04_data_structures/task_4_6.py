# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_s = ospf_route.split()
template = '''
{:25}{:25}
{:25}{:25}
{:25}{:25}
{:25}{:25}
{:25}{:25}
{:25}{:25}
'''
print(template.format("Protocol:","OSPF","Prefix:",ospf_s[1],"AD/Metric:",ospf_s[2].strip('[]'),"Next-Hop:",ospf_s[4].strip(','),"LastUpdate:",ospf_s[5].strip(','),"Outbount Interface:",ospf_s[6]))
