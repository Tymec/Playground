import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', type=str, help="Input csv document", dest="csv", required=True)
parser.add_argument('-o', type=str, help="Output document", dest="out", required=True)
parser.add_argument('-c', type=int, help="Column", metavar="col", dest="col", required=True)
parser.add_argument('-H', action='store_true', help="Has header row", dest="header_row")
args = parser.parse_args()

column_entries = []
with open(args.csv, 'r') as f:
    csv_doc = f.readlines()

i = 0
for line in csv_doc:
    i += 1
    if args.header_row:
        if i is 1:
            continue
    column_entries.append(line.split(',')[args.col - 1])
    
with open(args.out, 'w') as f:
    f.write('\n'.join(column_entries))