from typing import List

def count_unique_words(words: List[str]) -> int:
    # accepts a list of stirngs "words"
    my_set = set()

    for eachWord in words:
        my_set.add(eachWord)

    return len(my_set)

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
