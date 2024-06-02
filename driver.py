class Driver:
    """Base class for a generic driver. Inherit from this class when 
    implementing a new driver.

    Attributes:
        debug (bool): Whether to output debug messages to console.
    """

    def __init__(self, debug=False):
        """Initialize driver.
        
        Args:
            debug (bool): Whether to output debug messages, default False.
        """

        if debug: print("Driver: Initializing")
        self.debug = debug

        self._last_message = None
        self._connected = False

    def connect(self):
        """Connect to a device."""

        if self.debug: print("Driver: Connecting")
        self._connected = True

    def disconnect(self):
        """Disconnect from a device."""

        if self.debug: print("Driver: Disconnecting")
        self._connected = False

    def _read(self):
        """Template function for reading from a bus"""
        return
    
    def _write(self):
        """Template function for writing to a bus"""
        return

    def transmit(self, message):
        """Transmit a message to a device.
        
        Args:
            message (str): Message to send to device.
        """

        if self.debug: print("Driver: Transmitting message: {}".format(message))

        # Check if connected before transmitting
        if self._connected:
            self._last_message = message
        else:
            if self.debug: print("DRIVER ERROR: Not connected")

    def receive(self):
        """Receive a message from a device."""

        if self.debug: print("Driver: Receiving message")

        if self._connected:
            return self._last_message
        else:
            if self.debug: print("DRIVER ERROR: Not connected")
        



