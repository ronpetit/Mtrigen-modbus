import sys
import time
from pymodbus3.client.sync import ModbusTcpClient as ModbusClient
import ReadAndWriteRegisters as IO
import RPi.GPIO as GPIO
import os

RPMPageNumber = 4
RPMRegisterOffset = 6
DCCurrentPageNumber = 4
DCCurrentRegisterOffset = 207
STOP = 35700 #This are control keys
STOPC = 29835 #This are complements of control keys, must be write together with the control key
AUTO = 35701
AUTOC = 29834
MANUAL = 35702
MANUALC = 29833
AUTOM = 35704
AUTOMC = 29831
START = 35705
STARTC = 29830
RESETAL = 35734
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

host = sys.argv[1]
print("Connecting to DSE with IP ", host)
client = ModbusClient(str(host), port = 502)
client.connect()
time.sleep(0.1)

def main():
	try:
		print("Changing the DSE to manual mode, engine will start in 5 seconds")
		IO.write_register(MANUAL, MANUALC)
		
		x = 4
		while x>=1:
			time.sleep(1)
			print(str(x))
			x-=1

		print("Starting engine, and popup window will open to read RPM and load current")
		IO.write_register(START,STARTC)
		time.sleep(3)
		os.system('sudo xterm -hold -e "sudo python3 Monitor.py" &')
		print("Waiting for the engine to reach minimum speed")
		time.sleep(10)
		print("Governor speed control ON")
		PWM = GPIO.PWM(11, 100)
		Current = IO.read_register(DCCurrentPageNumber, DCCurrentRegisterOffset, 0.1)
		X = ((Current - 32)/88) * 100
		PWM.start(X)
		while 1==1:
			Current - IO.read_register(DCCurrentPageNumber, DCCurrentRegisterOffset, 0.1)
			X = ((Current -32)/88) * 100
			PWM.ChangeDutyCycle(X)

	except (KeyboardInterrupt, SystemExit):
		PWM.stop()
		GPIO.cleanup()
		print("Program stopped, cleaning up the GPIO ports")		

if __name__ == "__main__"
	main()	
	
