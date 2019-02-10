class A:
    def funcA(self):
        print('func A')


class B(A):
    def funcB(self):
        print('func B')


a = A()
a.funcA()

b = B()
b.funcA()
b.funcB()
