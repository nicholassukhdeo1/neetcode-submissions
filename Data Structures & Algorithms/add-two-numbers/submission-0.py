# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        num1 = []
        num2 = []

        temp1 = l1
        temp2 = l2

        while temp1 and temp2:
            insert_num = temp1.val + temp2.val
            num1.append(temp1.val)
            temp1 = temp1.next

        while temp2:
            num2.append(temp2.val)
            temp2 = temp2.next

        res = []

        # for value1, value2 in zip(num1,num2):
        #     insert_num = int(value1) + int(value2)
        #     print(F"these are my vals: {int(value1) + int(value2)}"
            # new_node = ListNode(insert_num)

        num1.reverse()
        num2.reverse()

        one = int("".join(map(str,num1)))
        two = int("".join(map(str,num2)))

        value = one + two

        my_str = str(value)

        print(f"my_str is {my_str}")

        new_node = ListNode()
        res = new_node

        print(f"str_len is {len(my_str)}")

        actual = my_str[::-1]
        print(f"actual is {actual}")

        for i in range(0,len(actual)):
            my_int = int(actual[i])
            print(f"my_int is {my_int}")
            new_node.next = ListNode(my_int)
            new_node = new_node.next


        return res.next