import sys

# try:
#     print("Hello, My name is", sys.argv[1])
# except:
#     print("Too Few Arguments")
    
    
# if len(sys.argv) < 2:
#     sys.exit("Too few argumnets")
# elif len(sys.argv) > 2:
#     sys.exit("Too many argumnets")

# print("Hello, my name is", sys.argv[1])

if len(sys.argv) < 2:
    print("Too few argumnets")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)