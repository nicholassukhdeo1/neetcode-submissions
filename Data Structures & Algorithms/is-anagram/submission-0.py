class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        strings = [s, t]
        
        letterMap = {}

        for currLetter in s:

            if currLetter not in letterMap:

                letterMap[currLetter] = 1

            else:

                letterMap[currLetter] += 1

        for currLetter in t:

            if currLetter not in letterMap:

                letterMap[currLetter] = 1
                return False

            else:

                letterMap[currLetter] -= 1

        for currLetter in t:
            if letterMap[currLetter] != 0:
                return False
        

        return True


    #then, we need to compare the hashmaps.
    #yeah, what if i make another variable to store the

        