import logging
from driver import Driver
from device import Device
import test_modes

logger = logging.getLogger(__name__)

class Tester():
    """Test system for supported hardware devices and protocols.
    
    Attributes:
        _test_device (Device): Device being tested.
        _test_Result (bool): Result of most recent test.
        _command (str): Most recent test mode.
    """

    def __init__(self, device: Device):
        """Initialize tester.
        
        Args:
            device (Device): Device being tested.
        """

        self._test_device = device
        self._test_result = False
        self._command = None

    def _validate_result(self):
        """Output test results to console."""

        if self.test_result:
            print("Tester: {} TEST PASS".format(self._test_mode))
        else:
            print("Tester: {} TEST FAIL".format(self._test_mode))

    def test_device(self, test_mode):
        """Run supported test procedures and validate the result.
        
        Args:
            test_mode (str): test_mode as selected from supported modes in messages.py.
        """
        
        logger.info("Test mode {}".format(test_mode))
        
        # Check if mode is valid
        if test_mode not in test_modes.MODES:
            logger.error("Test mode not recognized!")
            return
        
        # Transmit and receive test results
        self._test_mode = test_mode
        self._test_device.command_transmit(self._test_mode)
        self.test_result = (self._test_device.command_response() == self._test_mode)
        
        self._validate_result()


def sample_test_sequence():
    """A quick example of how to use the tester."""

    # Initialize driver and device address
    test_driver = Driver()
    test_address = 0

    # Initialize device, note that device is automatically connected
    test_device = Device(test_address, test_driver)
    
    # Initialize tester
    tester = Tester(test_device)   

    # Run any test modes requested
    tester.test_device(test_modes.MODE_FULL)
    tester.test_device(test_modes.MODE_QUICK)    

    # Shutdown device 
    test_device.shutdown()
 
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    sample_test_sequence()

