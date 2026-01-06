class NODE:
    def __init__(self,data):
        self.data=data
        self.next=None
class SINGLY_LINKED_LIST:
    def __init__(self):
        self.head=None
    def append(self,value):
        new_node=NODE(value)
        # self.node is my frist new node 
        if self.head==None:
            self.head=new_node
        
        else:
            current_value=self.head
            while current_value.next !=None:
                current_value=current_value.next
            current_value.next=new_node
    
    def traverse(self): 
        current_value = self.head
        while current_value!=None:
            
            
            print(f"{current_value.data} ->  " , end=" ")
            current_value = current_value.next
            
        print("None")
 
        # def insert(self,value,position):
    #     new_node=NODE(value)
    #     if position==0:
    #         new_node.next=self.head
    #         self.head=new_node
    #     else :
    #         current_node=self.head
    #         previous_node=current_node
    #         count=0
    #         while count<position and current_node is not None :
    #             previous_node=current_node
    #             current_node=current_node.next
    #             count+=1
    #         previous_node.next=new_node
    #         new_node.next=current_node

        
        
        
   # # def add_at_frist(self,frist_insert):
    # #     new_node=NODE(frist_insert)
    # #     new_node.next=self.head
    # #     self.head=new_node
    

