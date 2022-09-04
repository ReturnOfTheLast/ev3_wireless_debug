# EV3 wireless debugging program
As part of my P0 project at Aalborg University, I have chosen to write a quick and simple program that lets me debug the EV3 mindstorm in real time over an isolated selfhosted wifi network.

## Dependencies
- python3

## Installation Instructions
- Setup a WiFi network for the EV3 mindstorm and you to connect to (I used an raspberry pi with [RaspAp](https://raspap.com/))
- Clone this repository on the device that will be the server:
```sh
git clone https://github.com/ReturnOfTheLast/ev3_wireless_debug.git
```

## Usage
Run the `server.py` file:
```sh
python server.py
```

Then add the code from `client.py` to your EV3 micropython code.

**Remember** to change the `HOST` variable to the ip of your server.