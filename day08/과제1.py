class submitError(Exception):
    def __init__(self):
        super().__init__("This is Error")
        
try:
    raise submitError
except submitError as a:
    print(a)
    
