class ARRANGE  :
    def __init__(self,data):
        self.data=data
    def arrange_elements(self):
        low=0
        mid=0
        high=len(self.data)-1

        while mid<=high:
            if self.data[mid]==0:
                self.data[low],self.data[mid]=self.data[mid],self.data[low]
                low+=1
                mid+=1
            elif self.data[mid] == 1:
                mid += 1
            else:
                self.data[mid],self.data[high]=self.data[high],self.data[mid]
                high-=1
        return self.data
    
arr=[0,1,2,0,2,1]

change=ARRANGE(arr)

print(change.arrange_elements())
            