class MazeGame:
    def __init__(self, room_cls):
        self.rooms = []
        room1 = room_cls()
        room2 = room_cls()
        room1.connect(room2)
        self.rooms.append(room1)
        self.rooms.append(room2)


class MagicRoom:
    pass


class OrdinaryRoom:
    pass


ordinary_game = MazeGame(OrdinaryRoom)
magic_game = MazeGame(MagicRoom)
