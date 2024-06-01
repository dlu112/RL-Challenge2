# Driver implementation
# Methods:
#   Connection, Disconnection, Data Transmission, Reception

class Driver:
    def __init__(self, id):
        self.id = id

    def connect(self):
        print("Connect")

    def disconnect(self):
        print("Disconnect")

    def transmit(self, command):
        print("Transmitting ", command)

    def receive(self, reply):
        print("Receiving: ", reply)