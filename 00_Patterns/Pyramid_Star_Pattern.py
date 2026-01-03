class PYRAMID:
    def __init__(self,number):
        self.number=number
    def star_pattern(self):
        for i in range(1,self.number+1):
            space=self.number-i
            stars=2*i-1
            print(space*' '+stars*"x")

# data=5
# pattern=PYRAMID(data)
# pattern.star_pattern()