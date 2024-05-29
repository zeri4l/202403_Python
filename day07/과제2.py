class Animal:
    def __init__(self, name=""):
        self.name = name
        
    def cry(self):
        print("name")
        
        
class Tiger(Animal):
    def __init__(self):
        super().__init__()
        
    def cry(self):
        print("꽥꽥")
        
t= Tiger()
t.cry