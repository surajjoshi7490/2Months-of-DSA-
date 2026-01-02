class MAX_SUM:
    def __init__(self,data):
        self.data=data
    def max_k_sum(self,k):
        length_arr=len(self.data)

        current_sum=sum(self.data[:k])
        max_sum=current_sum
        if length_arr<k:
            return "Your array is too small "
        
        for i in range (length_arr-k):
            current_sum=current_sum-self.data[i]+self.data[i+k]

            if current_sum>max_sum:
                max_sum=current_sum

        return max_sum
    
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
solver = MAX_SUM(arr)
print(f"Max sum of {k} consecutive elements: {solver.max_k_sum(k)}")