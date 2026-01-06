from creating_singly_list import *

class SLL_INSERT(SINGLY_LINKED_LIST ):
    def insert_At(self, value, position):
        new_node=NODE(value)
        if position==0:
            new_node.next=self.head
            self.head=new_node
        else :
            previous=None
            current=self.head
            count=0
            while count<position and current !=None:
                previous=current
                current=current.next
                count+=1
            previous.next=new_node
            new_node.next=current
sll=SLL_INSERT()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.traverse()
sll.insert_At(25,2)
sll.traverse()


