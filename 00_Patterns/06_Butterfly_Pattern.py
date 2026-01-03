class BUTTERFLY_PATTERN:
    def  __init__(self,number):
        self.number=number
    def star_patter(self):
        for i in range(1,self.number):
            space=(2*self.number)-(i*2)
            print(i*'X'+space*" "+i*'X')
        for i in range(self.number,1,-1):
            space=(2*self.number)-(i*2)
            print(i*'X'+space*" "+i*'X')

data=5
pattern=BUTTERFLY_PATTERN(data)
pattern.star_patter()
