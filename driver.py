import logging
logger = logging.getLogger(__name__)
class Driver:
    """Base class for a generic driver. Inherit from this class when 
    implementing a new driver.
    """

    def __init__(self):
        """Initialize driver.
        """
        logger.info("Initializing")

        self._last_message = None
        self._connected = False

    def connect(self):
        """Connect to a device."""
        logger.info("Connecting")
        self._connected = True

    def disconnect(self):
        """Disconnect from a device."""
        logger.info("Disconnecting")
        self._connected = False

    def _read(self):
        """Template function for reading from a bus"""
        return
    
    def _write(self):
        """Template function for writing to a bus"""
        return

    def transmit(self, message, d_address):
        """Transmit a message to a device.
        
        Args:
            message (str): Message to send to device.
        """
        logger.info("Transmitting message: {}".format(message))
        logger.info("Target address: {}".format(d_address))


        # Check if connected before transmitting
        if self._connected:
            self._last_message = message
        else:
            logger.error("Not connected")

    def receive(self):
        """Receive a message from a device."""
        logger.info("Receiving message")

        if self._connected:
            # Sample return message for testing purposes
            return self._last_message
        else:
            logger.error("Not connected")
        



