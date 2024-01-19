# -*- coding: utf-8 -*-
"""access_data_extraction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FZAFcUa7FjZDpVzX9_ExFI4YRRE-yOlZ
"""

pip install fpdf

import requests
import json
import re
import os
from fpdf import FPDF
pdf = FPDF()

api_url = "https://operations-api.access-ci.org/wh2/cider/v1/access-allocated/"
response = requests.get(api_url)

if response.status_code == 200:
    # Request was successful
    json_data = response.json()
    print("success")
else:
    print("Failed to retrieve data from the API")

if os.path.exists("file1.txt"):
  os.remove("file1.txt")
for results in json_data['results']:
    print('Resource descriptive name: ', results['resource_descriptive_name'], sep='', end='.\n', file=open('file1.txt', 'a')),
    print(end='\n', file=open('file1.txt', 'a')),
    print('The resource description for ', results['resource_descriptive_name'], ' is the following: ', results['resource_description'],sep='', end='.\n', file=open('file1.txt', 'a')),
    print(end='\n', file=open('file1.txt', 'a')),
    print('The current status for ', results['resource_descriptive_name'], ' is the following: ', results['latest_status'],sep='', end='.\n', file=open('file1.txt', 'a')),
    print(results['resource_descriptive_name'], ' has been in its current status since ', results['latest_status_begin'],' and is expected to be in its current status until ', results['latest_status_end'], sep='', end='.\n', file=open('file1.txt', 'a')),
    print(end='\n', file=open('file1.txt', 'a')),
    print('The user guide url for ', results['resource_descriptive_name'], ' can be found at the following link: ', results['user_guide_url'],sep='', end='.\n', file=open('file1.txt', 'a')),
    print(end='\n', file=open('file1.txt', 'a')),
    print('The features list for ', results['resource_descriptive_name'], ' is the following: ', results['features_list'], sep='', end='.\n', file=open('file1.txt', 'a')),
    print(end='\n', file=open('file1.txt', 'a')),
    print('Other listed features include the following names and descriptions: ', sep='', file=open('file1.txt', 'a'))
    for features in results['features']:
        print(features['name'], ': ', features['description'], sep='', end='.\n', file=open('file1.txt', 'a'))
    print(end='\n', file=open('file1.txt', 'a')),
    print(end='\n', file=open('file1.txt', 'a'))

f = open("file1.txt", "r")

file = f.read()

file = re.sub("\[", "", file)
file = re.sub("\]", "", file)
file = re.sub('\u2019', "", file)
file = re.sub('\u201c', "", file)
file = re.sub('\u201d', "", file)
file = re.sub('\u2122', "", file)

f.close()

f= open("file2.txt", "w")
f.write(file)

f.close()

pdf.add_page()

pdf.set_font("Arial", size = 12)

f = open("file2.txt", "r")

# insert the text in pdf
for x in f:
    pdf.cell(200, 10, txt = x, ln = 1, align = 'L')

pdf.output("resources.pdf")