import startDSE
import time

while 1==1:
	time.sleep(2)
	print("Engine speed ", startDSE.RPMRegister, " RPM")
	print("DC load current ", startDSE.DCRegister, " A")
