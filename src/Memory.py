import array

MAX_MEMORY = 16000

class Memory:
	data = array.array('B', [0x00 for _ in range(MAX_MEMORY)])

	def write_byte(self, address, value):
		self.data[address] = value

	def read_byte(self, address):
		return hex(self.data[address])

	def read_address(self, address):
		return hex(int(hex(self.data[address+1] << 8),16) + int(hex(self.data[address]),16))

	def log_bytes(self, start_address, length):
		print(f"Memory dump - start address: {start_address} Bytes: {length}")
		for i in range(start_address,length):
			print(f"{self.data[i]:02x} ", end="")
			if (i+1) % 8 == 0: print("")

if __name__ == "__main__":
	ram = Memory()
	ram.write_byte(0x0001, 0x42)
	ram.write_byte(0x0002, 0x69)
	ram.log_bytes(0x00, 16)
	print(ram.read_byte(0x0002))
	print(ram.read_address(0x0001))

