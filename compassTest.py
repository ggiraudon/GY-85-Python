import sys,os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/i2clibraries")
from i2c_hmc5883l import *

hmc5883l = i2c_hmc5883l(port=1,addr=0x1e)

hmc5883l.setContinuousMode ()
hmc5883l.setDeclination (2,4)

while True:
    print(hmc5883l) 
    sleep(0.1)
