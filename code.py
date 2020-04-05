# This code drives a simple circuit that engages the shutter 
# in single-frame mode on my super 8 camera.
# It uses a heart rate monitor (Pulse Sensor Amped https://www.adafruit.com/product/1093)
# as analog input to an Adafruit ItsyBitsy. The signal from the monitor 
# sets the voltage at pin A1, which is read and when it's within a certain
# value range, pin D7 is triggered to close the shutter circuit. 
# Pin D5 acts as an indicator so I can see when the monitor's signal has
# settled into an accurate reading of my pulse, before I engage the camera.

from analogio import AnalogIn
import board
import digitalio
import time

analog_in = AnalogIn(board.A1)

# Camera shutter circuit
#
# pin D7 set to True/1 drives a 
# transistor switch closing the shutter circuit
camera = digitalio.DigitalInOut(board.D7)
camera.direction = digitalio.Direction.OUTPUT

# Indicator LED showing output from heart monitor
#
# helpful to watch the monitor stabilize (or not)
# before turning on the camera circuit
indicator = digitalio.DigitalInOut(board.D5)
indicator.direction = digitalio.Direction.OUTPUT

while True:
	plottable = analog_in.value/10
	if 3600 < plottable < 4000:
		camera.value = 1
		indicator.value = 1
	else:
		camera.value = 0
		indicator.value = 0

	print((plottable,))


	time.sleep(0.01)
