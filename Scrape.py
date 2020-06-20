"""
    This is a Code to scrape some certain part of a Text File
    from one file to another.

    Usage :
        Scrape.py  <inpur_file.txt>  <output_file.txt>

    Do replace the inline looping functions for matching the
    to scrape the content of your need!

    Liscense : GNU - OpenSource. (Do want you want to do!)

    IG : ravikiran.me
"""


import os
import sys

if len(sys.argv) <= 2 or len(sys.argv) > 3:
    print("Usage: \n\tScrape.py <input_file.txt> <output_file.txt> \n\tExit!")
else:
    file_in = sys.argv[1]

    fin = open(file_in, 'r', encoding='utf-8', errors='ignore')

    file_out = sys.argv[2]

    idx = 1
    f_name = str(idx) + "_" + file_out

    fout = open(f_name, 'w', encoding='utf-8', errors='ignore')

    for line in fin:
        if "BEGIN:" in line:
            fout.write(line.replace("\n", " "))
            try:
                while "END:" not in line:
                    line = next(fin)
                    fout.write(line.replace("\n", " "))
            except StopIteration:
                pass
            fout.write("\n" * 2)
