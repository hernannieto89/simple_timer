# simple_timer
Raspberry pi 3 simple timer for N way relay.

## Instalation
Requirements:
 - [Raspbian](https://www.raspberrypi.org/downloads/raspbian/)
 - [Python 2.7 +](https://www.python.org/)

Just clone repository and execute.
```
$ git clone https://github.com/hernannieto89/simple_timer
$ cd simple_timer
$ python main.py ...
```

## Description
When within certain time range provided by **start_time** and **end_time**, this script
turns on relays provided by **pins** (*GPIO BCM addresses list*) for certain **work_time**.
Then it turns off relays and sleeps for **sleep_time**.
If the program is outside the time range provided, It just waits for next day time range.
This loop is repeated indefinitely.
To terminate a keyboard interrupt or a sigterm signal is required.
This program is thought to run as a service.
##

## Warnings
Relay addresses need to be provided according to **GPIO BCM** format.
For more information please check this [link](https://es.pinout.xyz/).
This program is designed to work with 5v n way relays.
Do not try to execute this code with other modules. 
For more information please check this [link](https://www.youtube.com/watch?v=OQyntQLazMU).
Run it at your own risk.

## Usage
Execute main.py, several flags are required.
```
$ python main.py --pins 2 3 --start_time=12 --end_time=17 --work_time=60 --sleep_time=120
```
### pins
Space separated list with GPIO BCM address numbers. Integer list.

### start_time
Start hour of the day for timer. Accepts from 0 to 23. Integer.

### end_time
End hour of the day for timer. Accepts from 0 to 23. Integer.

### work_time
Relay connected time. Expressed in seconds. Integer.

### sleep_time
Relay idle time. Expressed in seconds. Integer.