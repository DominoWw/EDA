from slistH import SList
from slistH import SNode

class SList2(SList):
    def delLargestSeq(self):          
        '''This function deletes all the elements of the largest sequence of equal numbers from the calling list.'''
        node = self._head
        largest = 0
        current = 0
        pos = 0
        while node != None:

            if (current != node.elem):
                current = node.elem
                i = pos+1
                count = 0    
            node = node.next  
            count +=1
            pos += 1
            if (count >= largest):
                    largest = count
                    element = current
                    position = i-1  
        node = self._head
        i = 0
        fnode = None
        enode = None
        while node!= None:
            if position-1 == i:
                fnode = node
            if position+largest == i:
                enode = node
            i += 1
            node=node.next
        if fnode == None:
            self._head = enode
        else:
            if enode != None:   
                fnode.next = enode
            else:
                fnode.next = None
        self._size -= largest
        #return element, position, largest
        return self

    def create_loop(self, position):
        if position < 0 or position > len(self) - 1:
            raise ValueError(f"Position out of range [{0} - {len(self) - 1}]")

        current = self._head
        i = 0

        # We reach position to save the reference
        while current and i < position:
            current = current.next
            i += 1

        # We reach to tail node and set the loop
        start_node = current
        print(f"Creating a loop starting from {start_node.elem}")
        while current.next:
            current = current.next        
        current.next = start_node

    # This is the trickiest part: 
    # If we do it through nested loops we end up in an infinite loop unless we mark the nodes as visited somehow 
    # (maybe to make it simpler we could allow a python list to do so)
    def fix_loop(self):
        first = self._head
        print(first.elem)
        second = self._head
        while(first and second and second.next):       
            first = first.next
            print(first.elem)
            second = second.next.next            
            if second == first:
                self._break_loop(first)
                return True

        return False

    def _break_loop(self, node):
        print("Found loop, determining the start and the end of the loop")
        first = node
        second = node

        # We count the number of items in the loop
        count = 1 
        while(first.next != second):
            first = first.next
            count += 1

        # We find start and end
        first = self._head
        second = self._head

        # If list has length X and loop contains N elements, loop will start in position X - N - 1
        for _ in range(len(self) - count):
            first = first.next
            second = second.next

        # Now we move second pointer till the last position
        while second.next != first:
            second = second.next

        print(f"Found loop: {first.elem} - {second.elem}")
        second.next = None



    def leftrightShift(self,left,n):
        """This functions left-shift (left= True) or right (left=False) shifts the list by n nodes"""
    
        if self.isEmpty():
          print('The list is empty')
          return
        if n > len(self):
            print('Wrong n')
            return
        if n==len(self):
            return
        
        index = 0
        if left == True:
            """left shift"""
            index = n
        else:
            """right shift"""
            index = len(self) - n
          
        nodeIt=self._head
        nodePrev = None
        for i in range(index):
            nodePrev = nodeIt
            nodeIt=nodeIt.next
        
        nodeNewHead = nodeIt
        nodePrev.next = None
      
        while nodeIt and nodeIt.next:
           nodeIt=nodeIt.next
           
        nodeIt.next =  self._head
        self._head = nodeNewHead
            
    
    def __str__(self):
        """Returns a string with the elements of the list"""
        result=''                                   

        nodeIt=self._head                           

        while nodeIt!=None: #nodeIt!=None           
            result+=str(nodeIt.elem)+", "            
            nodeIt=nodeIt.next                      
        
        if len(result)>0:
            result=result.strip()                           
            result=result[:-1]                       
        
        return "["+result+"]"


if __name__=='__main__':

#    print('delLargestSeq()')
#    l = SList2()
#    for i in [3,3,3,4,5,6,6,6,7,7,7,7,2]:        
#        l.addLast(i)
#    print(l.delLargestSeq())
    
    '''
    l = SList2()
    for i in [8,8,8,8,4,5,6,6,6,6,6,6,7,7,7,2,2,2,2,2]:        
        l.addLast(i)
    print(l.delLargestSeq())

    l = SList2()
    for i in [1,1,1,3,4,5]:        
        l.addLast(i)
    print(l.delLargestSeq())
    print()
    print()

    '''

    print('fix_loop()')
    
    l=SList2()
    print("list:",str(l))
    print("len:",len(l))

    for i in range(7):
        l.addLast(i+1)

    print(l)
    print()

    # We force a loop
    l.create_loop(position=6)
    l.fix_loop()
    print("Loop fixed, changes applied")
    print(l)
    print()
    print()

'''
    print('leftrightShift()')
    l=SList2()
    for i in range(7):
         l.addLast(i+1)

    print(l)
    l.leftrightShift(False, 2)
    print(l)
'''