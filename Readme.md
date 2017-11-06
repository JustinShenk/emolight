Emolight
========

Convert emotions to LED colors on a Raspberry Pi. Demoed at Intel Global IoT DevFest.

This script can be used for controlling WS281X LED strips with a Raspberry Pi. Several wiring guides exist:
- https://learn.adafruit.com/neopixels-on-raspberry-pi/wiring
- http://dordnung.de/raspberrypi-ledstrip/

## Getting started

First install the [NeoPixel library](https://github.com/jgarff/rpi_ws281x#build). Also, install the Python bindings from the `python` directory:

```sh
sudo apt-get install python-dev swig
python ./setup.py build
```

Clone the repository:
```sh
git clone https://github.com/justinshenk/emolight.git
cd emolight
```

Install fswebcam with `sudo apt-get install fswebcam`.

Get a [Microsoft Emotion API key](https://azure.microsoft.com/en-us/try/cognitive-services/?api=emotion-api) (free trial).

For setting the light with a single image run
`sudo python emolight.py -s`

To run the script indefintely, run `sudo python emolight.py`

Run the script with a new image every minute with `sudo python emolight.py -d 60`

## TODO
 - [ ] Replace Microsoft API with local neural network implmentatoin
