class Infor:
    serialNumber = 0
    def __init__(self, name, age, ismale, number):
        self.__name = name
        self.__age = age
        self.__ismale = ismale
        Infor.serialNumber += 1      
        self.__number = Infor.serialNumber
        
    def getName(self):
        return self.__name
    
    def setAge(self, age):
        if age >= 1:
            self.__age = age
        else:
            print("나이는 한 살 이상이어야합니다.")
            
    
    
    def setIsmale(self, ismale):
        if ismale == "남성":
            ismale == True
        else:
            ismale == False
            
    def getIsmale(self):
        if ismale == True:
            return "남성"
        else:
            return "여성"

    
    def show(self):
        print(f'내 이름은 {self.__name}입니다. 나이는 {self.__age}살, 성별은 {self.__ismale}입니다.')
        
    def plusAge(self):
        self.__age += 1 
        
    def check_number(self, number):
        if number == Infor.serialNumber:
            return True
        else:
            return False
        
        
a= Infor("1", 2, "male", 1)

a.show()
a.plusAge()
a.show()

