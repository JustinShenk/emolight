moodlight
========

Convert emotions to LED colors on a Raspberry Pi (development stage). Demoed at Intel Global IoT DevFest.

This script can be used for controlling WS281X LED strips with a Raspberry Pi. Several wiring guides exist:
- https://learn.adafruit.com/neopixels-on-raspberry-pi/wiring
- http://dordnung.de/raspberrypi-ledstrip/

## Getting started

#### Install dependencies

First install the [rpi_ws281x Library](https://learn.adafruit.com/neopixels-on-raspberry-pi/software#compile-and-install-rpi-ws281x-library) on your Raspberry Pi.

Install some dependencies:

```sh
sudo apt-get update
sudo apt-get install build-essential python-dev git scons swig
```

Download the library source and compile it:
```sh
git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons
```

Now install the Python library from the `rpi_ws281x/python` directory.

```sh
cd python
python ./setup.py build
```

#### Fetch moodlight

Clone the repository install dependencies:
```sh
git clone https://github.com/justinshenk/moodlight.git
cd moodlight
pip install -r requirements.txt
cp config.ini.example config.ini
```

#### Webcam
If using a webcam, install fswebcam with `sudo apt-get install fswebcam`.

#### Emotion Detection
Get a [Microsoft Emotion API key](https://azure.microsoft.com/en-us/try/cognitive-services/?api=emotion-api) (free trial) and add your key to `MY_API` in `config.ini`.

#### Start moodlight
For setting the LED strip with a single image run
`sudo python moodlight.py -s`.

To run the script indefinitely, run `sudo python moodlight.py`.

Run the script with a new image every minute with `sudo python moodlight.py -d 60`.

## TODO
 - [ ] Add local neural network implementation (eg, Caffe)
 - [ ] Add Google Cloud Vision API
 - [ ] Add picamera support
 - [ ] Add make file
 - [ ] Add color fading option
