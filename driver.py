class Driver:
    """
    Base class for a generic driver. Inherit from this class when 
    implementing a new driver.
    """

    def __init__(self):
        self.debug = False
        if self.debug: print("Initializing driver")

    def connect(self):
        if self.debug: print("Connecting")

    def disconnect(self):
        if self.debug: print("Disconnecting")

    def transmit(self, message):
        if self.debug: print("Transmitting message: {}".format(message))

    def receive(self):
        if self.debug: print("Receiving message")



