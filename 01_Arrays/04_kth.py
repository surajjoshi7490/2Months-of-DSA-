class KTH :
    def __init__(self,data):
        self.data=data
        
    def K_th(self,k):
        if k>len(self.data) or k<=0:
            return None, None
        
        smallest=self.data[k-1]
        largest=self.data[len(self.data)-k]

        return smallest, largest
    
arr=[1,30,20,40,70,60,50,90,80]
arr.sort()
element=KTH(arr)

k =3

s,l=element.K_th(k)
print(s,l)

# Time Complexity is O(n Log n ) Because we have used sort()
# Space Complexity is O(1)