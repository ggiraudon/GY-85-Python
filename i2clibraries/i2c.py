import time
import smbus

class i2c:
	
	def __init__(self, port, addr, debug = False):
		self.bus = smbus.SMBus(port)
		self.addr = addr
		self.debug = debug
		
	def write_byte(self, *bytes):
		self.bus.write_byte_data(self.addr, *bytes)
				
	def read_byte(self, register):
		byte = self.bus.read_i2c_block_data(self.addr, register, 1)[0]
		return byte
	
	def read_16bit(self, register, flip = False):
		data = self.bus.read_i2c_block_data(self.addr, register, 2)
		
		if flip:
			bit16 = (data[1] << 8) | data[0]
		else:
			bit16 = (data[0] << 8) | data[1]
		
		if self.debug:
			print(hex(register)+": "+hex(bit16));
			
		return bit16
	
	def read_s16int(self, register, flip = False):
		s_int = self.read_16bit(register, flip)
		return self.twosToInt(s_int, 16)
	
	def read_3s16int(self, register, flip = False):
		data = self.bus.read_i2c_block_data(self.addr, register, 6)
			
		if self.debug:
			print("3 signed 16: %s " % ', '.join(map(hex, data)))
			
		if flip:
			s_int1 = (data[1] << 8) | data[0]
		else:
			s_int1 = (data[0] << 8) | data[1]
			
		if flip:
			s_int2 = (data[3] << 8) | data[2]
		else:
			s_int2 = (data[2] << 8) | data[3]
			
		if flip:
			s_int3 = (data[5] << 8) | data[4]
		else:
			s_int3 = (data[4] << 8) | data[5]
			
		return (self.twosToInt(s_int1, 16), self.twosToInt(s_int2, 16), self.twosToInt(s_int3, 16) )
													
	def twosToInt(self, val, len):
		# Convert twos compliment to integer
		if(val & (1 << len - 1)):
			val = val - (1<<len)
			
		if self.debug:
			print(str(val))
		return val
													
