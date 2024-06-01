# RL-Challenge2

## Objective
Develop a software system using Python to test hardware devices that support the
same commands but various communication protocols such as Ethernet, RS-422, or RS-485. All devices accept string commands and return the same string to indicate successful command execution. The software should support two testing procedures, QUICK and FULL tests.

## Design considerations

Device class
Methods: Initialization, Shutdown, Command Transmission, Command Response reception
Modes: QUCK, FULL
--> Driver can be passed via dependency injection

Driver class
Methods: Connection, Disconnection, Data Transmission, Reception

Communication protocols: Ethernet, RS-422, RS-485, other?
--> Class needs to be a prototype