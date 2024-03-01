import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/i2clibraries")
from i2c_adxl345 import *
from time import *

adxl345 = i2c_adxl345(1)

while True:
    print (adxl345)
    sleep (0.1)
