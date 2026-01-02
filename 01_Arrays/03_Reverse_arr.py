class  REVERSE_ARR:
        def __init__(self,data):
                self.data=data

        def reverse_array(self):
                if not self.data:
                        return None
                starting=0
                ending=len(self.data)-1

                while starting<ending:
                        self.data[starting] , self.data[ending] = self.data[ending], self.data[starting]

                        starting+=1
                        ending-=1

                return self.data 
        
arr=[1,2,3,4,5,6,7,8,9,10]

tracker=REVERSE_ARR(arr)

print(tracker.reverse_array())

# Time complexity is O(n) because of the loop 
# Space complexity is O(1) because all variable contains single value 