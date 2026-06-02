class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # count with a dictionary first

        count_dict = defaultdict(int)

        for num in nums: # key: number, value: count
            count_dict[num] += 1

        my_list = list(count_dict.items())

        

        my_list.sort(key=lambda x: x[1], reverse=True)

        return [x[0] for x in my_list[:k]] #first element for every tuple
        # in my_list filled with tuples.


        # return kth top frequent elements




        