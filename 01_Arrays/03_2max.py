class TOP_TWO_MAX:
    def __init__(self,data):
        self.data=data
    def two_max(self):
        if not self.data:
            return None,None
        
        max1=float("-inf")
        max2=float('-inf')

        for i in self.data:
            if i>max1:
                max2=max1
                max1=i
            elif i>max2:
                max2=i
        return max1,max2
    
arr=[10,20,40,21,32,89,30,8,1]

top=TOP_TWO_MAX(arr)
Top1,Top2=top.two_max()
print(Top1,Top2)

# Space Complexity is O(1)
# Time complecity is O(n)