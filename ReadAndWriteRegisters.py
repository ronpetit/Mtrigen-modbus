import sys
import time
from pymodbus3.client.sync import ModbusTcpClient as ModbusClient

def sync_client_read(registerNumber):
	try:
		result = client.read_holding_registers(registerNumber,1)
		return result.registers
	except:
		print("Connection Error Handled")
		output = False
	return output

def read_register(PageNumber, RegisterOffset, Scale):
	register = 256 * PageNumber + RegisterOffset
	read = sync_client_read(register)
	register = float(read) * Scale
return register

def write_register(SystemControlKeys, ComplimentControlKey):
	wr = client.write_registers(4104, [SystemControlKeys, ComplimentControlKey])
return True	
