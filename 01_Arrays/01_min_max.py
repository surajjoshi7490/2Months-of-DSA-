class MIN_MAX:
    def __init__(self,arr):
        self.arr_n=arr
        
    def find_min_max(self):
       if not self.arr_n:
           return None,None
       
       current_min=self.arr_n[0]
       current_max=self.arr_n[0]

       for i in range(1,len(self.arr_n)):
           if self.arr_n[i] < current_min:
               current_min=self.arr_n[i]
           elif self.arr_n[i]>current_max:
               current_max=self.arr_n[i]
            
       return current_max,current_min
        

data=[1,2,3,4,5,6,7,8,9,10]

tracker=MIN_MAX(data)

minnium,maximmum=tracker.find_min_max()

print(tracker.find_min_max())

# Space complexity is O(1) becase all of the valriable are fixed 
# Time Copmlixity is 0(n) because of the loop 