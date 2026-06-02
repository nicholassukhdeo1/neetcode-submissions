class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make a dictionary where you have sorted keys
        # and the values are the actual words

        my_dict = defaultdict(list)

        for word in strs:
            my_dict[tuple(sorted(word))].append(word)

        return list(my_dict.values()) 