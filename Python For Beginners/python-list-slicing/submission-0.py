from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    
    new_list = [0] * 3
    new_list[2] = my_list[-1]
    new_list[1] = my_list[-2]
    new_list[0] = my_list[-3]
    return new_list

    # 


# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
