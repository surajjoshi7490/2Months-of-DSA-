from creating_singly_list import *

class DELETE(SINGLY_LINKED_LIST):
    def delete_first(self):
        if self.head is None:
            raise Exception (" List is empty")
        self.head=self.head.next 
        
sll=DELETE()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)
sll.append(6)
sll.traverse()
sll.delete_first()
sll.traverse()