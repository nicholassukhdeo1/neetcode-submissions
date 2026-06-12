class Solution:
    def isValid(self, s: str) -> bool:
        # we can do that pop method


        my_stack = []

        # (... )

        # stack: blank

        # stack: [
        # stack: blank (after you remove cuz of match)

        for char in s:
            if char == "(" or char == "{" or char == "[":
                my_stack.append(char)
            elif char == ")":
                if len(my_stack) == 0:
                    return False #nothing to pair w/
                if my_stack[-1] != "(":
                    return False

                my_stack.pop()
            elif char == "}":
                if len(my_stack) == 0:
                    return False #nothing to pair w/
                if my_stack[-1] != "{":
                    return False
            
                my_stack.pop()
            elif char == "]":
                if len(my_stack) == 0:
                    return False #nothing to pair w/
                if my_stack[-1] != "[":
                    return False
                
                my_stack.pop()

            

        #when you see an opening bracket, add to stack
        #when you see closing, remove


        # cuz this will make an array
        if len(my_stack) != 0:
            return False
        return True


        # cuz if we are able to pass the if checks
        # enough times, for the list to be zero, then we are good

        # maybe check if you have set in first place

        # whatever i see, i add 