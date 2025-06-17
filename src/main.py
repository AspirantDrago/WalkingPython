import os
import sys

path = ' '.join(sys.argv[1:])
for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        print(os.path.join(dirpath, filename))
