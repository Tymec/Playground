import os
import argparse

parser = argparse.ArgumentParser(description='Bookmarks to links')
parser.add_argument('-f', '--file', help="Path to file", dest="file", metavar="file", required=True)
args = vars(parser.parse_args())

in_file = args["file"]
out_file = "C:\\Users\\Tymek11rt\\Desktop\\out.txt"
bookmarks = []

with open(in_file, 'r', encoding="utf8") as f:
    for line in tuple(f):
        if "HREF" in str(line):
            split_txt = str(line).split("\"")[1]
            bookmarks.append(split_txt)
            
with open(out_file, 'w', 1, encoding="utf8") as f:
    out = ""
    for line in bookmarks:
        out += line + "\n"
    f.write(out)