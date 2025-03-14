import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]

    matches = re.findall(r'\b' + re.escape(keyword) + r'\b', text)

    if matches:
        print(len(matches))
    else:
        print("none")
