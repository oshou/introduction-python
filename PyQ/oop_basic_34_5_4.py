from oop_basic_34_5_2 import StatCount
from oop_basic_34_5_3 import StatTime


class RoomCounter:
    def __init__(self):
        self.__num_air = StatCount()
        self.__num_room = StatTime()

    def room_in(self, num):
        self.__num_air.assign(num)
        self.__num_room.assign(self.__num_room.get_value() + num)

    def room_out(self):
        self.__num_room.assign(self.__num_room.get_value() - 1)

    def show_mean(self):
        print('エアシャワーの利用人数の回数平均: ', self.__num_air.get_mean())
        print('工場内の人数の時間平均', self.__num_room.get_mean())


def simulate():

    StatTime.Time = 9
    rc = RoomCounter()
    rc.room_in(4)

    StatTime.Time = 12
    for _ in range(4):
        rc.room_out()
    rc.room_in(1)

    StatTime.Time = 13
    rc.room_in(1)

    StatTime.Time = 14
    rc.show_mean()


simulate()
