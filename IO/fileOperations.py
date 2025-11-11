try:
    with open('./dummy.txt', "r") as f:
        data = f.read()
        print(data)
except FileNotFoundError as fne:
    print(fne)

#modes in file operations
# r - read
# w - write
# rb - read binary
# wb - write binary
# a - append to existing
# x - create a new file