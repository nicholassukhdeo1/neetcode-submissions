def first_n_characters(s: str, n: int) -> str:
    return s[:n] #starts at 0, ends at n

def last_n_characters(s: str, n: int) -> str:
    # start at last n chars..
    # so that means

    # NeetCode
    # start at index 5 if we want the final 3 chars

    index = len(s) - n
    return s[index:] #starts at n, ends at final char


# do not modify below this line
print(first_n_characters("NeetCode", 3))
print(first_n_characters("NeetCode", 4))
print(first_n_characters("NeetCode", 8))

print(last_n_characters("NeetCode", 3))
print(last_n_characters("NeetCode", 4))
print(last_n_characters("NeetCode", 8))
