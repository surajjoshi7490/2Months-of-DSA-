class DOWNWARD:
    def __init__(self,number):
        self.number=number
    def star_pattern(self):
        for i in range(self.number,0,-1):
            print(i*"X")

data=7
pattern=DOWNWARD(data)
pattern.star_pattern()