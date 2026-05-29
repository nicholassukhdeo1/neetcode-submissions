from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    my_dict = {}

    # count the occurrences of each letter in a word

    for letter in word: #dont overwrite keys
        if letter not in my_dict:
            my_dict[letter] = 1
        else:
            my_dict[letter] += 1

    return my_dict




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))