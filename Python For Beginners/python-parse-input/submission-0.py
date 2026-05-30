from typing import List

def read_integers() -> List[int]:
    my_string = input()
    split_string = my_string.split(",")
    i = 0
    for number in split_string:
        split_string[i] = int(number)
        i += 1
    return split_string

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
