class INVERTED_PYRAMID:
    def __init__(self,number):
        self.number=number
    def inverted_pattern(self):
        
        for i in range (1,self.number):
            stars=2*i-1
            spaces=self.number-i
            if i==1:
                print(" "*spaces + "X")
            else :       
                print(' '*spaces+"X" + (stars - 2)*' ' + "X")

        for i in range(self.number,0,-1):
            stars=2*i-1
            spaces=self.number-i
            
            if i==1:
                print(" "*spaces + "X")
            else :       
                print(' '*spaces+"X" + (stars - 2)*' ' + "X")
       
    
data=11

pattern=INVERTED_PYRAMID(data)
pattern.inverted_pattern()


