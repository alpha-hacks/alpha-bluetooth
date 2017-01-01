# alpha-bluetooth
UBTECH alpha robot comunication software (www.ubtrobot.com/)

## Bluetooth

[Buetooth protocol PDF](Alpha1 Series Bluetooth communication protocol565212.pdf)

> Note: In the Attribute column "W" indicates write; "R" indicates read; and "A" indicates automatic report of BT

- [ ] BT handshake (R)
- [ ] Obtaining an action list (R)
- [ ] Implementing an action list (W)
- [ ] Play stop (W)
- [ ] Sound switch (W)
- [ ] Play control (W)
- [ ] Heartbeat packet (W)
- [ ] Reading robot state (R/A)
- [ ] Volume adjustment (W)
- [ ] Powering off all servos (W)
- [ ] Controlling all servo indicators (W)
- [ ] Clock calibration (W)
- [ ] Reading clock parameters (R)
- [ ] Setting clock parameters  (W)
- [ ] Reading the software version (R)
- [x] Reading battery capacity of the robot (R)
- [ ] Low voltage alarm (A)
- [ ] Reading the hardware version number of the robot (R)
- [ ] Controlling the motion of a single servo (W)
- [ ] Controlling the motion of multiple servos (W)
- [ ] Reading back angle of a single servo (powered off) (R)
- [ ] Reading back angle of multiple servos (powered off) (R)
- [ ] Setting offset value of a single servo (W)
- [ ] Setting offset value of multiple servos (W)
- [ ] Reading offset value of a single servo (R)
- [ ] Reading offset value of multiple servos (R)
- [ ] Reading version of a single servo (R)
- [ ] Reading version of multiple servos (R)
- [ ] Play completion (A)
- [ ] Allowing charge during play (W/A)
- [ ] Reading the SN of the robot (R)
- [ ] Reading the UDID of the main chip (R)
- [ ] Sending the action list (A)
- [ ] Completing action list sending (A)




### Dependencies

```sh
sudo apt-get install libbluetooth-dev
pip3 install -r requirements.txt
```
### Test

```sh
python3 main.py
```

[Buetooth protocol PDF URL](http://www.ubtrobot.com/upload/download/Alpha1%20Series%20Bluetooth%20communication%20protocol565212.pdf)
