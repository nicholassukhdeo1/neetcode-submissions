class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        


        # a car arrived after how much time?

        stack = []
        cars = {}

        for pos, speed in zip(position, speed):
            cars[pos] = speed

        sorted_cars = dict(sorted(cars.items()))

        print(sorted_cars)

        # how to remember whose speed is what

        for pos, speed in sorted_cars.items():
            dist_left = target - pos
            time = dist_left / speed

            while stack and time >= stack[-1]:
                stack.pop()



            stack.append(time)


        return len(stack)




            # if they arrived at same time, then 



        # if a car behind arrives quicker than a car in front of it
        # it would match