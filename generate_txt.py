# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 12:39:12 2024
Program to take complete "entry" class data for applications/centers
and convert to text file
@author: moelg
"""
import os


def build_new_dict(soft_database):
    new_dict = {}
    for k, v in soft_database.items():
        # print(k, v)
        # print(v.short_name)
        # print(v.centers)
        if v.short_name not in new_dict:
            # print('1', v.short_name, v.centers)
            # print(new_dict)
            new_dict[v.short_name] = set(v.centers)
            # new_dict[v.short_name] = new_dict[v.short_name].add(v.centers)
        else:
            if v.centers not in new_dict[v.short_name]:
                # print('2', v.short_name, v.centers)
                # print(new_dict)
                temp = new_dict[v.short_name]
                temp.update(v.centers)
                new_dict[v.short_name] = temp
                # new_dict[v.short_name] = new_dict[v.short_name].add(v.centers)
        # new_dict[v.short_name].extend(v.centers)
    return new_dict


def make_txt_doc(soft_database):
    software_database = build_new_dict(soft_database)
    if os.path.exists("software_by_application.txt"):
        os.remove("software_by_application.txt")
    print('Software on ACCESS Resource Providers Grouped by Application Name', '\n',
          file = open('software_by_application.txt', 'a'))
    # for key in software_database:
    #     print(key, ': These Resource Providers(clusters) have the ', key, ' software installed: ', sep='', end='',
    #           file=open('software_by_application.txt', 'a'))
    #     accumulator = 0
    #     for value in software_database[key]:
    #         length = len(software_database[key])
    #         if accumulator >= length - 1 and length != 1:
    #             print('and ', end='', file=open('software_by_application.txt', 'a'))
    #             print(value, end='. ', file=open('software_by_application.txt', 'a'))
    #         elif accumulator == 0 and length == 2:
    #             print(value, end=' ', file=open('software_by_application.txt', 'a'))
    #         elif not accumulator >= length - 1 and length != 1:
    #             print(value, end=', ', file=open('software_by_application.txt', 'a'))
    #         else:
    #             print(value, end='. ', file=open('software_by_application.txt', 'a'))
    #
    #         accumulator += 1
    #     print('\n', end='', file=open('software_by_application.txt', 'a'))
    #     print('\n', end='', file=open('software_by_application.txt', 'a'))

    for key in software_database:
        print(key, ': ', sep='', end='', file=open('software_by_application.txt', 'a'))
        count = 1
        for value in software_database[key]:
            length = len(software_database[key])
            if length == 1:
                print(value, ' has the ', key, ' software installed.', sep='', end='', file =open('software_by_application.txt', 'a'))
            elif count == 1 and length ==2:
                print(value, ' and ', sep='', end='', file=open('software_by_application.txt', 'a'))
            elif count < length - 1:
                print(value, ', ', sep='', end='', file=open('software_by_application.txt', 'a'))
            elif count == length - 1:
                print(value, ', and ', sep='', end='', file=open('software_by_application.txt', 'a'))
            else:
                print(value, ' have the ', key, ' software installed.', sep='', end='', file=open('software_by_application.txt', 'a'))
            count += 1
        print('\n', end='', file=open('software_by_application.txt', 'a'))
        print('\n', end='', file=open('software_by_application.txt', 'a'))
