class Registers:
	__regs = {"A": 0x00, "B": 0x00, "C": 0x00, "D": 0x00, "E": 0x00, "H": 0x00, "L": 0x00}

	def write_register(self, register, value):
		self.__regs[register] = value

	def read_register(self, register):
		return self.__regs[register]

	def read_HL(self):
		return self,