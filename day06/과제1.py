class Infor:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show(self):
        print(f'내 이름은 {self.name}입니다. 나이는 {self.age}살, 성별은 {self.gender}입니다.')
        
    def plusAge(self):
        self.age += 1 
        
a= Infor("1", 2, "male")

a.show()
a.plusAge()
a.show()
