# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:45:22 2024
Definition of software application "entry" class
@author: moelg
"""


class entry:
    short_name = ''
    long_name = ''
    centers = set()

    # create constructor
    def __init__(self, short_name, long_name, center):
        if not short_name:  # if string has anything in it returns True
            raise ValueError('short_name is empty')
        if not long_name:
            raise ValueError('long_name is empty')
        if not center:
            raise ValueError('center is empty')
        self.short_name = short_name
        self.long_name = long_name
        self.centers = {center}

    def __repr__(self):
        return '[' + self.short_name + '; ' + self.long_name + '; ' + ' '.join(self.centers) + ']'

    def __str__(self):
        return '[' + self.short_name + '; ' + self.long_name + '; ' + ' '.join(self.centers) + ']'
