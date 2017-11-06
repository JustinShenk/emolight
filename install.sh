#!/bin/bash

install_rpi-ws281x="sudo apt-get update &&
sudo apt-get install build-essential \
  python-dev git scons swig &&
echo 'rpi_ws281x will be installed in your home directory' &&
echo -n 'Install rpi_ws281x in [~/] (y/n)?: '
read YES_NO
if [ '$YES_NO' == 'y' ]
then
  cd ~/ &&
  git clone https://github.com/jgarff/rpi_ws281x.git
  cd rpi_ws281x
  scons
  cd python
  python ./setup.py build
  git clone https://github.com/justinshenk/emolight.git
  cd emolight
  pip install -r requirements.txt
else
  echo 'Please specify installation directory.'
fi"
pip list | grep rpi-ws281x && echo "rpi-ws281x already installed" || `install_rpi-ws281x`
