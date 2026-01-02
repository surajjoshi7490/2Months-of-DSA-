class ARRANGE:
    def __init__(self,data):
        self.data=data
    def move_negative(self):
        left=0
        for right in range(len(self.data)):
            if self.data[right] <0:
                self.data[left],self.data[right]=self.data[right],self.data[left]
                left+=1
        return self.data
arr=[-1,6,-9,2,8,-10]

ordered=ARRANGE(arr)

print(ordered.move_negative())

# here Time complixity is O(n)
# space complexity is 0(1)
# but the catch is that order of the negative are changed 