from typing import List

def contains_duplicate(words: List[str]) -> bool:
    # if your list/array isnt IDENTICAL to ur set
    # there is a duplicate

    my_set = set()

    for eachElement in words:
        my_set.add(eachElement)
    
    if len(my_set) == len(words):
        return False

    return True

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
