from driver import Driver
import messages

class Device:
    """
    Base class for a generic device. Inherit from this class when  
    implementing a new device.
    """

    def __init__(self, driver: Driver, d_address):
        self._driver = driver
        self._d_address = d_address

        self._last_command = None
        self.mode = messages.MODE_OFF

        self.debug = False

        self._driver.connect()

    def shutdown(self):
        self._driver.disconnect()

    def command_transmit(self, command):
        self.mode = command
        self._driver.transmit(command)

    def command_response(self):
        reply = self.driver.receive()
        return reply

