import sys
import re

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    for i in args:
        if re.match(r".*ism$", i):
            continue
        else:
            print(i + "ism")
