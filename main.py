#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Feb 19 13:23:13 2024
Program to fetch ACCESS Software Discovery API data
regarding applications installed on various computing
centers and convert application/center data to text file
@author: moelg
"""

if __name__ == "__main__":
    import database_parser
    import get_api_data
    import generate_txt

    software_discovery_data = get_api_data.extract_api_data()
    initial_soft_database = database_parser.parse_data(software_discovery_data)
    complete_soft_database = database_parser.create_short_name(initial_soft_database)
    generate_txt.make_txt_doc(complete_soft_database)

##Below code is for rough debugging
    # toy_json_data = {
    #     'results': [
    #         {
    #             'Type': 'Executable Software',
    #             'Name': 'gcc',
    #             'Relations': [
    #                 {
    #                     'RelationType': 'Hosted On',
    #                     'Name': 'Delta'
    #                 }
    #             ]
    #
    #         }
    #
    #     ]
    # }
    #
    # toy_json_data2 = {
    #     'results':
    #         [
    #             {
    #                 'Type': 'Executable Software',
    #                 'Name': 'gcc',
    #                 'Relations': [
    #                     {
    #                         'RelationType': 'Hosted On',
    #                         'Name': 'Delta'
    #                     }
    #                 ]
    #             },
    #             {
    #                 'Type': 'Executable Software',
    #                 'Name': 'anaconda3',
    #                 'Relations': [
    #                     {
    #                         'RelationType': 'Hosted On',
    #                         'Name': 'Ookami'
    #                     }
    #                 ]
    #             }
    #         ]
    # }
    #
    # toy_json_data3 = {
    #     'results': [
    #         {
    #             'Type': 'Executable Software',
    #             'Name': 'gcc',
    #             'Relations': [
    #                 {
    #                     'RelationType': 'Hosted On',
    #                     'Name': 'Delta'
    #                 }
    #             ]
    #         },
    #         {
    #             'Type': 'Executable Software',
    #             'Name': 'gcc13',
    #             'Relations': [
    #                 {
    #                     'RelationType': 'Hosted On',
    #                     'Name': 'Ookami'
    #                 }
    #             ]
    #         },
    #         {
    #             'Type': 'Executable Software',
    #             'Name': 'anaconda3',
    #             'Relations': [
    #                 {
    #                     'RelationType': 'Hosted On',
    #                     'Name': 'Stampede3'
    #                 }
    #             ]
    #         }
    #     ]
    # }
    #
    # toy_json_data4 = {
    #     'results':
    #         [
    #             {
    #                 'Type': 'Executable Software',
    #                 'Name': 'gcc',
    #                 'Relations': [
    #                     {
    #                         'RelationType': 'Hosted On',
    #                         'Name': 'Delta'
    #                     }
    #                 ]
    #             },
    #             {
    #                 'Type': 'Executable Software',
    #                 'Name': 'gcc',
    #                 'Relations': [
    #                     {
    #                         'RelationType': 'Hosted On',
    #                         'Name': 'Ookami'
    #                     }
    #                 ]
    #             }
    #         ]
    # }

    ###tests with toy data

    # print(extract_center({
    #     'Type': 'Executable Software',
    #     'Name': 'gcc',
    #     'Relations': [
    #         {
    #             'RelationType': 'Hosted On',
    #             'Name': 'Delta'
    #         }
    #     ]
    #
    # }))
    #
    # try:
    #     extract_center({
    #         'Type': 'Executable Software',
    #         'Name': 'gcc',
    #         'Relations': [
    #             {
    #                 'RelationType': '',
    #                 'Name': 'Delta'
    #             }
    #         ]
    #
    #     })
    # except:
    #     print('It worked!')
    #
    # print(extract_center({
    #     'Type': 'Executable Software',
    #     'Name': 'gcc',
    #     'Relations': [
    #         {
    #             'RelationType': '',
    #             'Name': 'Delta'
    #         },
    #         {
    #             'RelationType': 'Hosted On',
    #             'Name': 'Delta'
    #         }
    #     ]
    # }))
    #
    # print(extract_software({
    #     'Type': 'Executable Software',
    #     'Name': 'gcc',
    #     'Relations': [
    #         {
    #             'RelationType': 'Hosted On',
    #             'Name': 'Delta'
    #         }
    #     ]
    #
    # }))
    #
    # try:
    #     extract_software({
    #         'Type': '',
    #         'Name': 'gcc',
    #         'Relations': [
    #             {
    #                 'RelationType': 'Hosted On',
    #                 'Name': 'Delta'
    #             }
    #         ]
    #
    #     })
    # except:
    #     print('It worked!')


    # initial_soft_database = database_parser.parse_data(toy_json_data3)
    # print(initial_soft_database)
    # print(sorted(initial_soft_database.items()))
    # print(type(sorted(initial_soft_database.items())))
    # print(complete_soft_database)

