class Sample1:
    name = 'name'


print(Sample1.name)
Sample1.name = 'changed_name'
print(Sample1.name)
print()


class Sample2:
    def __init__(self, value):
        self.value = value


s1 = Sample2('AAA')
s2 = Sample2('BBB')
print(s1.value)
print(s2.value)
s1.value = 'CCC'
print(s1.value)
print(s2.value)
