# GY-85-Python
Interfacing with GY-85 (IMU module) with Python
This is a fork from fhd-codes/GY-85_Raspberry-Pi with a few tweaks


# Step 1: Install smbus

- Option 1 (Debian based systems):

      $ sudo apt-get install python3-smbus -y

- Option 2 (Using pip):

      $ pip3 install smbus
        

# Step 2: Connect GY-85 and checking the connection

- Connect GY-85 with Raspberry Pi.

  Connect **3.3v, GND, SCL, SDA** pins on GY-85 with the corresponding pins on your SBC/machine

- Open terminal and write:

      $ sudo i2cdetect -y 1
   
   where **1** is the i2c bus number (try i2cdetect -l for a list of busses).
   
   A table will appear which will show the address of connected devices. The sensors have following addresses:
   
   Accelerometer(ADXL): **53**
   
   Gyroscope(ITG): **68**
   
   Compass(HMC): **1e**
   
   
# Step 5: Downloading the code files

- Open the terminal and download the code files

      $ git clone https://github.com/ggiraudon/GY-85-Python.git
      
# Getting the values from Gyro, Acc, and Compass

- Run the following files to get the data:
  
  gyroTest.py     
  
  accTest.py     
  
  compassTest.py
  
  
      $ git clone 
      
 
  **Note:** If the output from __*compassTest.py*__ is giving 0 values, it means that GY-85 module has QMC5883l instead of HMC5883l. In that case, please refer to https://github.com/fhd-codes/GY-85_Raspberry-Pi.git for more details
  
 
# Main reference sources:

- Code is collected from these sources.
  
  [source1](https://topic.alibabacloud.com/a/raspberry-pi-connects-9-axis-imu-sensor-gy-85-module_8_8_32153608.html)
  
  [source2](https://elinux.org/RPi_ADC_I2C_Python)
  
  [source3](https://topic.alibabacloud.com/a/raspberry-pi-connects-9-axis-imu-sensor-gy-85-module_8_8_32153608.html)
  
  [source4](http://www.knight-of-pi.org/installing-python3-6-on-a-raspberry-pi/)

  [source5](https://github.com/fhd-codes/GY-85_Raspberry-Pi.git)
