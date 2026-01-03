class STAR_PATTERN:
    def __init__(self,number):
        self.number=number
    def pattern(self):
        for i in range(self.number):
            print(self.number*'x')
        return 
data=5
star=STAR_PATTERN(data)
star.pattern()