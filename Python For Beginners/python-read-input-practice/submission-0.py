def add_two_numbers() -> int:
    input_text = input()

    raw_string = input_text.split(",")

    numbers = []

    numbers.append(int(raw_string[0]))
    numbers.append(int(raw_string[1]))

    return numbers[0] + numbers[1]



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
