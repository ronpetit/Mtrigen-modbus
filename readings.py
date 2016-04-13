import startDSE as DSE
import time

while 1==1:
	time.sleep(2)
	print("Engine speed ", DSE.main().RPMRegister, " RPM")
	print("DC load current ", DSE.main().DCRegister, " A")
