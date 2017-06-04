#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""
bobs = 0
count = 0
for i in s:
    if s[count:count+3] == 'bob':
        bobs += 1
    count += 1
print('Number of times bob occurs is: ' + str(bobs))
