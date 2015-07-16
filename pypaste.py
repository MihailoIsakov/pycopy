#! /usr/bin/env python

import os
import argparse
import subprocess

inputs = open(os.path.expanduser('~/.pycopy/clipboard.txt'), 'r')
for line in inputs.readlines():
    input_name = line.rstrip()
    cur_path = os.path.abspath('.')
    
    command = "cp -r " + input_name + " " + cur_path
    
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
