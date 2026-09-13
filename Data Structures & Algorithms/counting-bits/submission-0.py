class Solution:
    def countBits(self, n: int) -> List[int]:


        output = []
        count = 0
        

        for value in range(0,n+1):
            while value != 0:
                if value & 1 == 1:
                    count += 1
                value = value >> 1

            output.append(count)
            count = 0


        return output

            