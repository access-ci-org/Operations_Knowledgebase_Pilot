# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 12:09:23 2024
Program to extract ACCESS software discvovery API data
@author: moelg
"""
import requests


def extract_api_data():
    api_url = "https://operations-api.access-ci.org/wh2/resource/v4/resource_esearch/?affiliations=access-ci.org&page_size=300000&resource_groups=software"
    response = requests.get(api_url)

    if response.status_code == 200:
        # Request was successful
        json_data = response.json()
        print("success")
    else:
        print("Failed to retrieve data from the API")

    # print(json.dumps(json_data, indent = 4))
    return json_data
