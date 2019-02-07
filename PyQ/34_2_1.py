class Human:
    def __init__(self, age=0, last_name='', first_name='', blood_type=''):
        self.age = age
        self.last_name = last_name
        self.first_name = first_name
        self.blood_type = blood_type


h1 = Human()
h2 = Human(33, '田中', '一郎', 'O')

print(h1.age, h1.last_name, h1.first_name, h1.blood_type)
print(h2.age, h2.last_name, h2.first_name, h2.blood_type)
