# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:50:44 2024
Program to parse JSON data and create database of application/center data using "entry" class
@author: moelg
"""
import entry
from operator import itemgetter, attrgetter


def clean_name(name):
    return name.strip().lower()

def extract_center(resource):
    for relations in resource['Relations']:
        if relations['RelationType'] == 'Hosted On':
            return relations['Name']
    raise ValueError('Center not found in resource')


def extract_software(resource):
    if resource['Type'] == 'Executable Software':
        soft = clean_name(resource['Name'])
        center = extract_center(resource)
        return entry.entry(soft, soft, center)
    raise ValueError('Resource is not software')


def get_short_name(software_entry):
    return software_entry.short_name


def get_long_name(software_entry):
    return software_entry.long_name


def parse_data(json_data):
    software_database = dict()
    for resource in json_data['results']:
        # print(resource)
        try:
            software_instance = extract_software(resource)
        except ValueError:
            pass
        else:
            soft_short = software_instance.short_name
            if soft_short in software_database:
                software_database[soft_short].centers.update(software_instance.centers)
                # software_database[soft_short] gives the value where the key is defined
                # value.centers.add(software_instance.centers)
                # value is an entry
            else:
                software_database[soft_short] = software_instance
    return software_database

def de_duplicate_names(software_database):
    short_name_list = sorted([k for k,v in software_database.items()])
    current_app = 'zzz'
    new_short_name_list = list()
    for value in short_name_list:
        if value.startswith(current_app):
            pass
        else:
            current_app = value
            new_short_name_list.append(value)
    return new_short_name_list

def create_short_name(software_database):
    short_list = de_duplicate_names(software_database)
    for key, value in software_database.items():
        for software_app in short_list:
            if key == software_app:
                pass
            elif key.startswith(software_app): #de duplicate
                value.short_name = software_app
            else:
                pass
    return software_database


    # current_app = ''
    # for key, value in sorted(software_database.items(), key=lambda e: e.long_name):
    #     if value.soft_short.startswith(current_app):
    #         value.soft_short = current_app
    #     else:
    #         current_app = value.soft_short
    ##problem: software_database.items() is a tuple object no longer an entry object
    ##proposed solution: sort first, then iterate through software entries directly changing e.short_name?
    # software_nested_list = sorted(software_database.items())
    # for value in software_nested_list:
    #     #print(value[1][0]) #error: entry object is not subscriptable
    #     print(value)
    #     print(type(value))
    #     if value[1][0].get_short_name.startswith(current_app): #error: entry object is not subscriptable
    #         value[1][0].short_name = current_app
    #     else:
    #         current_app = software_nested_list[0].short_name
    # return software_nested_list
    # return software_dictionary
