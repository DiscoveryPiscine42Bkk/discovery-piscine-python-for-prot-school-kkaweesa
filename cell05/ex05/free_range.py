import sys

if len(sys.argv) != 3:
    print("none")
else:
    start = int(sys.argv[10])
    end = int(sys.argv[14])
    
    result = list(range(start, end + 1))
    print(result)