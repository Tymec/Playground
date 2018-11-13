import os
import glob
import argparse
import json

parser = argparse.ArgumentParser(description='Files from a path to paths in json file')
parser.add_argument('-p', '--path', help="Path to scan for", dest="path", metavar="path", required=True)
parser.add_argument('-a', '--amount', help="Amount of files to dump", dest="am", metavar="am", required=True)
args = vars(parser.parse_args())

ex_ext = [".db"]
file_list = glob.glob(args["path"] + "\\*")
for file in file_list:
    for ext in ex_ext:
        if ext in file:
            file_list.remove(file)
            
file_list.sort(key=lambda x: os.path.getmtime(x))

output = []

for i in range(1, int(args["am"])):
    output.append(file_list[-i])

with open("output.json", 'w') as f:
    json.dump(output, f, indent=4)

