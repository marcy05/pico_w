# Getting started

This is the how to used for the usage of Raspberry PI Pico W in Ubuntu 22.04 LTS

# MicroPython

In order to be able to connect to the board after the firmware installation you need to change the r/w permission with

```
sudo chmod 666 /dev/ttyACM0
```

reference
>https://stackoverflow.com/questions/27858041/oserror-errno-13-permission-denied-dev-ttyacm0-using-pyserial-from-pyth
