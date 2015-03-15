import sys
import re

# Show usage
if len(sys.argv) != 2:
	s = """Usage:  python avg.py LOGFILENAME"""
	print(s)
	sys.exit()

# OK here's the script proper	
logfile = sys.argv[1]
total = 0.0	# All warnings
i = 0 


with open(logfile, 'r') as logf:
	for l in logf:
		line = l.rstrip()
		elems = line.split(",")
		if len(elems) == 5 :
			num = float(elems[4][1:-1])
			total = total + num
			i = i + 1

print("Total time: " + str(total) + " - Average = " + str(total / i) + " total tests " + str(i))
			

		