from european_socket import EuropeanSocket


class Adapter(EuropeanSocket):
    def __init__(self, usa_socket):
        self.usa_socket = usa_socket

    def plug_in(self):
        return self.usa_socket.insert()
