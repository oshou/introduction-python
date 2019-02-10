class RoomCounter:
    def __init__(self):
        self._num_air = 0
        self._num_room = 0

    def room_in(self, num):
        self._num_air = num
        self._num_room += num

    def room_out(self):
        self._num_room -= 1

    def num_air(self):
        return self._num_air

    def num_room(self):
        return self._num_room


rc = RoomCounter()
rc.room_in(3)
rc.room_out()

print(rc.num_air())
print(rc.num_room())
