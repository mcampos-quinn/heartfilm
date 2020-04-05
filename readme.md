# heartfilm <3

This code drives a simple circuit that engages the shutter 
in single-frame mode on my super 8 camera.

It uses a heart rate monitor ([Pulse Sensor Amped](https://www.adafruit.com/product/1093)) as analog input to an Adafruit [ItsyBitsy](https://learn.adafruit.com/introducing-itsy-bitsy-m0/pinouts). The signal from the monitor sets the voltage at pin A1, which is read and when it's within a certain value range, pin D7 is triggered to close the shutter circuit. 

Pin D5 acts as an indicator so I can see when the monitor's signal has settled into an accurate reading of my pulse, before I engage the camera.

We'll see what comes of it!