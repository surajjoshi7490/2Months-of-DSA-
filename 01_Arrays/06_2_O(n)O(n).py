class ARRANGE :
    def __init__(self,data):
        self.data=data
    def move_negative(self):

        negative=[x for x in self.data if x<0]
        positive=[x for x in self.data if x>=0]

        self.data=negative+positive
        return self.data
    
arr=[-1,6,-9,2,8,-10]

tool=ARRANGE(arr)
print(tool.move_negative())

# Space complexity is O(n) because we are inserting and moving the data 
# time complexity is O(n) because we are using loops ORDERS ARE RESERVED