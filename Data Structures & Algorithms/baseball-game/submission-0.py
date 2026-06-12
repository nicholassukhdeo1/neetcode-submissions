class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # if ur array operations has a number like 2
        # record that 2 as a new score
        # + means add the two past scores
        # D means double previous score
        # C means invalidate previous score

        # sum up everything in ur record array

        record = []

        arr_length = len(operations)
        for i in range(arr_length):
            if operations[i] == "C":
                record.pop()
            elif operations[i] == "+":
                record.append(record[-1]+record[-2])
            elif operations[i] == "D":
                record.append(record[-1]*2)
            elif int(operations[i]) >= -30000 or int(operations[i]) <= 30000:
                record.append(int(operations[i]))

        sum = 0

        for num in record:
            sum += num

        return sum