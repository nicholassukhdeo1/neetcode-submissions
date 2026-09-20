class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = []
        stack = []

        size = len(temperatures)

        result = [0 for i in range(size)]

        for day_index in range(0,size):
            while stack and temperatures[day_index] > temperatures[stack[-1]]:
                index = stack.pop()
                count = day_index - index
                result[index] = count
            stack.append(day_index)

            nday_index = day_index + 1

            

        while stack:
            set_zero = stack.pop()
            result[set_zero] = 0

        return result


