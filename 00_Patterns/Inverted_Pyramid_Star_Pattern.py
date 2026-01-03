class INVERTED_PYRAMID:
    def __init__(self,number):
        self.number=number
    def inverted_pattern(self):
        for i in range(self.number,0,-1):
            stars=2*i-1
            spaces=self.number-i
            print(' '*spaces+stars*'x')
    
# data=5

# pattern=INVERTED_PYRAMID(data)
# pattern.inverted_pattern()


