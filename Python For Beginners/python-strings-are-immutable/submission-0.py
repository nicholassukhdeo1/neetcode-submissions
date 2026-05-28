def remove_fourth_character(word: str) -> str:
    newString = word[:3] + word[4:]
    return newString


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
