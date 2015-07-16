#! /usr/bin/env python

import argparse
import os

def main():
    parser = argparse.ArgumentParser(description = "Copy file path to clipboard")
    parser.add_argument("files", 
            nargs='+')
    
    args = parser.parse_args()
    cur_dir = os.getcwd()
    
    home_dir = open(
            os.path.expanduser('~/.pycopy/clipboard.txt'), 
            'w')
    for file in args.files:
        home_dir.write(cur_dir + '/' + file)
        home_dir.write("\n")

if __name__ == "__main__":
    main()
