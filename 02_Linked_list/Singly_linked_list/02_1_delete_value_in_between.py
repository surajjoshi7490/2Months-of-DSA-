from creating_singly_list import *

class DELETE_VALUE(SINGLY_LINKED_LIST):
    def delete_value(self,val):
        
        if self.head is None:
            raise Exception("List is empty")
        
        if self.head.data==val:
            self.data=self.data.next
            return
        else :
            
            previous=self.head
            current=self.head.next

            while current.data != val:
                previous=current
                current=current.next
                
            previous.next=current.next
            
sll=DELETE_VALUE()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)
sll.append(6)
sll.traverse()
sll.delete_value(3)
sll.traverse()

        