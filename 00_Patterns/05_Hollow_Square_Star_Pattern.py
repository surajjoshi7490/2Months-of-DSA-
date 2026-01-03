class HOLLOW_SQUARE:
    def __init__(self,number):
        self.number=number
    def square_pattern(self):
        for i in range(1,self.number+1):
            space=self.number-2
            if i==1 or i==self.number:
                print(self.number*"x")
            else :
                print("x"+space*' '+'x')

data=10
pattern=HOLLOW_SQUARE(data)
pattern.square_pattern()