class A:
    def __init__(self):
        self.name = 'Class A'


class B(A):
    pass


b = B()
print(b.name)

a = A()
print(a.name)
