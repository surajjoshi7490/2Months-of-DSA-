class MISSING_NUMBER():
    def __init__(self,data,number):
        self.data=data
        self.number=number
    def find(self):
        expected_sum=self.number*(self.number+1)//2

        tota_arr=sum(self.data)

        return expected_sum-tota_arr
    
arr=[1,3,4,5,6,7,8,9]
N=9
values=MISSING_NUMBER(arr,N)
print(values.find())
        
# here the time complexity is O(n)
# space complexity is O(1)