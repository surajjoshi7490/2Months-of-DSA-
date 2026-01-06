class CROSS_STAR:
    def __init__(self,number):
        self.number=number
    def star_patten(self):
        for i in range(self.number,1,-1):
            stars=2*i-1
            spaces=self.number-i
            
            if i==1:
                print(" "*spaces + "X")
            else :       
                print(' '*spaces+"X" + (stars - 2)*' ' + "X")
        for i in range (1,self.number,):
            stars=2*i-1
            spaces=self.number-i
            if i==1:
                print(" "*spaces + "X")
            else :       
                print(' '*spaces+"X" + (stars - 2)*' ' + "X")
data=7
pattern=CROSS_STAR(data)
pattern.star_patten()