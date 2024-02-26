from canlib import canlib, Frame


class CanController:
    def __init__(self) -> None:
        self.ch_a = canlib.openChannel(channel=0, flags=canlib.Open.ACCEPT_VIRTUAL)
        self.ch_a.setBusParams(canlib.canBITRATE_250K)
        self.master_id = 0x009
        self.slave_id = 0x018
        pass

    def connect(self):
        self.ch_a.busOn()
        print("connect")

    def disconnect(self):
        self.ch_a.busOff()
        self.ch_a.close()
        print("disconnect")

    def read_data(self):
        msg = self.ch_a.read(timeout=500)
        print(msg)
        print("read_data")
        return 42

    def save_data(self, data):
        msg=[0xFF, 69, 76, 76, 79, 33]
        self.send_msg(self.master_id, msg)
        print(f"saved data: , {data}")

    def send_msg(self, id, msg):
        frame = Frame(id_=id, data=msg)
        self.ch_a.write(frame)