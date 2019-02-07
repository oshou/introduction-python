class Sample:
    num = 100

    def get_my_self(self):
        return self

    def show_num(self):
        num = 200
        print(self.num)
        print(num)


a = Sample()
b = a.get_my_self()
print(a is b)
a.show_num()
