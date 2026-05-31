from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    my_map = defaultdict(int)

    for letter in s:
        my_map[letter] += 1

    return my_map


def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    # returns dictionary where keys are first elements of each list
    # values are rest of elements in list

    my_map = defaultdict(list) #cuz the values will be lists

    # you need 1 to have 2,3,4... cuz the other list is 

    for num_list in nums:
        if len(my_map[num_list[0]]) == 0:
            my_map[num_list[0]] = num_list[1:]
        else:
            my_map[num_list[0]] += num_list[1:]

    return my_map


# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
