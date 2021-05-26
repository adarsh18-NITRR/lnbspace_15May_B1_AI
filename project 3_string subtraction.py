class s2:
    def __init__(self,data):
        self.data = data
        print('created')
    def __sub__(self,obj):
        for i in obj.data:
            if i in self.data:
                j = (self.data).find(i)
                self.data = self.data[0:j] + self.data[j+1:]
        print(self.data)
        
        
        
x = s2('this is a test string')
y = s2('iii')
x - y