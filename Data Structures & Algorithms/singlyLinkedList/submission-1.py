class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    
    # O(n), worst case.. you walk through whole list an
    def get(self, index: int) -> int:
        
        #make ur temp object equal to self's head

        if index >= self.size: 
            return -1

        temp = self.head

        
        # you need to walk through the linkedlist
        # until u find what you want
        for i in range(index):

            #keep advancing temp until u reach right temp val
            temp = temp.next


        
        return temp.val
        
    # O(1)
    def insertHead(self, val: int) -> None:

        #empty list

        temp = Node(val)

        if self.head == None:
            self.head = temp
            self.tail = temp



        #non-empty list
        else:
            temp.next = self.head
            self.head = temp

        self.size += 1
            

        
    # O(n)
    def insertTail(self, val: int) -> None:

        temp = Node(val)

        if self.tail == None:
            self.head = temp
            self.tail = temp
            self.size += 1

        else:
            self.tail.next = temp
            self.tail = temp
            self.size += 1
        

    def remove(self, index: int) -> bool:

    #if you put in some weird index that doesnt apply.
        if index >= self.size:
            return False

    #if index is 0, easy money. just work with head
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return True

    # you need two pointers, think about it
    # you need to preserve the next pointer for the prior node.

    # how do i go forward here? without another loop

        temp = self.head
        beforeTemp = self.head

        temp = temp.next
        
        for i in range(index-1):
            beforeTemp = beforeTemp.next
            temp = temp.next

            
        if temp == self.tail:
            self.tail = beforeTemp

        beforeTemp.next = temp.next
        self.size -= 1
        return True

    def getValues(self) -> List[int]:

        # make an array with all of its values
        temp = self.head

        arr = []


        while temp is not None:
            arr.append(temp.val)
            temp = temp.next

        return arr
        
