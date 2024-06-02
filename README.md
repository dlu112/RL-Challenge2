# RL-Challenge2

## Objective
Develop a software system using Python to test hardware devices that support the
same commands but various communication protocols such as Ethernet, RS-422, or RS-485. All devices accept string commands and return the same string to indicate successful command execution. The software should support two testing procedures, QUICK and FULL tests.

## Implementation
This system implements three classes, a generic Device class, a generic Driver class, and a generic Tester class.

The Device class acts as a surface level interface for interacting with a hardware device, and contains the necessary functions for initializing, shutting down, transmitting, and receiving from a device. This class requries the address of the device and a Driver instance to be passed to it on creation. By default the Device class connects to the device on instantiation. Each function in Device is left public, and this class can be expanded on when implementing for a specific type of device.

The Driver class acts as a serial level interface for communicating with a hardware device, and contains the necessary functions for connecting, disconnecting, transmitting, and receiving from a device. These functions are currently left as shell functions and are designed to be expanded on when implementing a child class for a specific communcation protocol. In the parent class simple logic is left in place for testing and logic purposes. For example, the Driver.receive function is currently set to return the last message received. Empty private functions for reading and writing are also provided as placeholders. 

The Tester class acts as an implementation of the supported test procedures, and contains the necessary functions for testing a device and validating the results. This class requires a fully initialized Device object to be passed to it on instantiation. A Tester.test_device function is provided and the specified mode of test can be called with it to run a supported test procedure. A sample test sequence function is provided as an example of how to use the Tester in its current implementation.

A `test_modes.py` file is included with constants for supported test modes to ensure consistent language between the classes. When adding a new test mode, the constant name and a response message can be added to the file and then to the MODES array, which is used to easily identify valid test modes.

## Future extensions
The Device class is currently limited in what commands it can send via the Driver. A more robust system of sending validated commands can be implemented to allow for other functions as desired, as per the requirements of each specific device. Additionally, the current implementation requires a previously initialized Driver object to be passed to it on instantiation, and this can be expanded on in the future if a device needs to be instantiated without a known Driver and initialized later.

The Tester class can be expanded on to support additional types of tests by modifying the `test_modes.py` file. Different testing procedures for specifically the Device and Driver interactions could be implemented as well in the future to ensure working software-level behaviour. The test validation procedure can be altered to log to a logfile instead of to console. 

## Running the code
This system is written in python3.10.5 and requires no building. Documentation is provided in the class descriptions for where functions can be modified and inherited from for specific device and protocol implementations, and enough logic is left in place for a sample test sequence to run. The sample test sequence is located at the bottom of the `tester.py` file and can be run by running the file directly. Debug is set to True in the implementation to see the full extent of debug messages.