import sys

args = sys.argv[1:]

if len(args) != 1:
    print("none")
else:
    text = args[0]
    count_z = text.count("z")
    if count_z == 0:
        print("none")
    else:
        print("z" * count_z)
