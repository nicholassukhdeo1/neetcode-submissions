from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        insert_tuple = (timestamp,value)

        self.storage[key].append(insert_tuple)
        

    def get(self, key: str, timestamp: int) -> str:

        my_array = self.storage[key]

        L = 0
        R = len(my_array) - 1
        res = ""



        while L <= R:
            mid = (L+R) // 2

            if my_array[mid][1] != "" and my_array[mid][0] <= timestamp:
                res = my_array[mid][1]
                L = mid + 1
            elif my_array[mid][0] > timestamp:
                R = mid - 1

        return res
        
