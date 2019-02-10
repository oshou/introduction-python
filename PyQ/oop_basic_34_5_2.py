class StatCount:
    def __init__(self):
        self.__value = 0
        self.__count = 0
        self.__sum = 0

    def assign(self, value):
        self.__value = value
        self.__count += 1
        self.__sum += value

    def get_value(self):
        return self.__value

    def get_count(self):
        return self.__count

    def get_sum(self):
        return self.__sum

    def set_sum(self, value):
        self.__sum = value

    def get_mean(self):
        return self.__sum / max(1, self.__count)


def do_test():
    i = StatCount()
    i.assign(10)
    i.assign(20)
    print(i.get_value())
    print(i.get_count())
    print(i.get_mean())


if __name__ == '__main__':
    do_test()
