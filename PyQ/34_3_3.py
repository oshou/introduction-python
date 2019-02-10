class Sample:
    num1 = 100
    __num2 = 200

    def __init__(self):
        self.__num3 = 300

    def show_num(self):
        print(Sample.__num2)
        print(self.__num3)


print(Sample.num1)
# print(Sample.__num2)
s = Sample()
s.show_num()
# print(s.__num3)
