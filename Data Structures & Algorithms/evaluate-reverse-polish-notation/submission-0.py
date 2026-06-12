class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # only add numbers to your stack

        my_stack = []

        for element in tokens:
            if element == "+":
                # remember ur number to add
                num_to_add = my_stack[-1] + my_stack[-2]
                my_stack.pop()
                my_stack.pop()

                # so now, you dont pop the calc'd num
                my_stack.append(num_to_add)
            elif element == "-":
                # remember ur number to add
                num_to_add = my_stack[-2] - my_stack[-1]
                my_stack.pop()
                my_stack.pop()

                # so now, you dont pop the calc'd num
                my_stack.append(num_to_add)
            elif element == "*":
                # remember ur number to add
                num_to_add = my_stack[-1] * my_stack[-2]
                my_stack.pop()
                my_stack.pop()

                # so now, you dont pop the calc'd num
                my_stack.append(num_to_add)
            elif element == "/":
                # remember ur number to add
                num_to_add = int(my_stack[-2] / my_stack[-1])
                my_stack.pop()
                my_stack.pop()

                # so now, you dont pop the calc'd num
                my_stack.append(num_to_add)
            elif int(element) >= -200 or int(element) <= 200:
                my_stack.append(int(element)) # add ur numbers

        return my_stack[-1]