#!/usr/bin/env python
import os
import sys

path = "./"

s = r"""dirs:
- title: """

s_url = r"""
  url: """

s_tag = r"""
  tag: """
  
s_connect = r"""
- title: """

path += sys.argv[1]
files = os.listdir(path)
v = []
count = 0
m = {}
for name in files:
    if os.path.isdir(path+name):
        count += 1
        v.append(name)

#file_list = [[""] for i in range(0, count)]
s += v[0]
s += s_url
s += path  + v[0]
for i in range(1, count):
    s += s_connect
    s += v[i]
#    s += s_url
#    s += path + v[i]
    s+= s_tag
    s+= v[i]

f = open('./_data/dirs_list.yaml', 'w')
f.write(s)
f.close()
