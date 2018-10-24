import os

in_file = "C:\\Users\\Tymek11rt\\Desktop\\bookmarks_10_18_18.html"
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