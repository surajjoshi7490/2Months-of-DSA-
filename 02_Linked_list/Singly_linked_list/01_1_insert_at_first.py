from creating_singly_list import *

class INSERT_FIRST(SINGLY_LINKED_LIST):
    def insert_first(self,value):
        new_value=NODE(value)
        new_value.next=self.head
        self.head=new_value
    
sll=INSERT_FIRST()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)
sll.append(6)
sll.traverse()
sll.insert_first(10)
sll.traverse()

