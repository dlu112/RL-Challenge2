from driver import Driver

class Device:
    """Base class for a generic device. Inherit from this class when  
    implementing a new device.

    Attributes:
        d_address (int): Address of device.
        driver (Driver): Driver for device protocol.
        debug (bool): Whether to output debug messages to console.
        _last_command (str): Most recent command sent
    """

    def __init__(self, d_address, driver : Driver, debug = False):
        """Initialize device.
        
        Args:
            d_address (int): Address of device.
            driver (Driver): Driver for device protocol.
            debug (bool): Whether to output debug messages, default False.
        """

        if debug: print("Device: Initializing device")

        self.debug = debug
        self._d_address = d_address
        self._driver = driver

        self._last_command = None

        # initialize driver on startup
        self.initialize()

    def initialize(self):
        """Connect driver to device."""

        if self.debug: print("Device: Connecting driver")
        self._driver.connect()

    def shutdown(self):
        """Disconnect driver from device."""

        if self.debug: print("Device: Shutting down")
        self._driver.disconnect()

    def command_transmit(self, command):
        """Transmit a command via the driver.
        
        Args: 
            command (str): Command to send to device.
        """

        if self.debug: print("Device: Transmitting command {}".format(command))
        self._driver.transmit(command, self._d_address)

    def command_response(self):
        """Receive a message via the driver.
        
        Returns:
            The reply recieved by the driver as a string.
        """

        reply = self._driver.receive()
        if self.debug: print("Device: receiving message {}".format(reply))
        
        return reply

