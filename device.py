# Device implementation
# Methods:
#   Initialization, Shutdown, Command Transmission, Command Respone reception
# Modes:
#   QUICK, FULL

from driver import Driver

class Device:
    def __init__(self, id, protocol, driver: Driver):
        self.id = id
        self.protocol = protocol
        self.driver = driver
        self.mode = 0


    def shutdown(self):
        print("Shutdown")

    def com_transmit(self):
        print("Command Transmission")

        # Receive a command and enter execution mode

    def com_response(self):
        print("Command Response")

        # Return response to driver



    