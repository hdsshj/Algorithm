class Person :
  def __init__(self, param_name):
    print("i am created", self)
    self.name = param_name
    
  def talk(self) :
    print('안녕 하세요, 제 이름은', self.name, '입니다.' )
person1 = Person('우서크')
print(person1.name)
person1.talk()
person2 = Person('준서크')
print(person2.name)
person2.talk()
