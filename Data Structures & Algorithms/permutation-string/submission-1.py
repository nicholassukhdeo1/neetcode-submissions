class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        L = 0
        R = len(s1)
        s1map = Counter(s1)

        print(f"s1 contains: {s1map}")


        while R <= len(s2):
            substr = s2[L:R]
            substr_map = Counter(substr)

            print(f"s2 contains: {substr_map}")

            if s1map == substr_map:
                return True

            L += 1
            R += 1


        return False
