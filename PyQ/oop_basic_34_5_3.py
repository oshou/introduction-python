from oop_basic_34_5_2 import StatCount


class StatTime(StatCount):
    Time = 0

    def __init__(self):
        super().__init__()
        self.__initime = StatTime.Time
        self.__pretime = 0

    def assign(self, value):
        t = StatTime.Time - self.__pretime
        self.__pretime = StatTime.Time
        s = self.get_sum() + self.get_value()*t
        super().assign(value)
        self.set_sum(s)

    def get_mean(self):
        t = StatTime.Time - self.__pretime
        s = self.get_sum() + self.get_value() * t
        return s / (StatTime.Time - self.__initime)


def do_test():
    StatTime.Time = 9
    t = StatTime()
    t.assign(1)
    StatTime.Time = 11
    t.assign(4)
    print(t.get_mean())
    StatTime.Time = 12
    print(t.get_mean())


if __name__ == '__main__':
    do_test()
