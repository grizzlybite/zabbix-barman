#!/usr/bin/env python3
# coding: utf8

import subprocess
import json

value = {'data':[]}
barman_list = subprocess.Popen(['barman','list-server'], stdout=subprocess.PIPE) 
for line in barman_list.stdout:
    server = (line.decode().replace("\n","")).split(' ')[0]
    value['data'].append({'{#SERVER}':server})

print (json.dumps(value))

