import sys
import re

# Show usage
if len(sys.argv) != 2:
	s = """Usage:  python warnings.py LOGFILENAME"""
	print(s)
	sys.exit()

# OK here's the script proper	
logfile = sys.argv[1]
total = 0	# All warnings
filecount = dict()

print("Listing warnings for log file:  " + logfile)
pattern = re.compile("^\d+\>(?P<filename>.*)\(\d+\) : warning")
with open(logfile, 'r') as logf:
	for l in logf:
		line = l.rstrip()
		match = re.search(pattern, line)
		if match:
			total = total + 1
			afile = match.group("filename")
			if afile in filecount:
				filecount[afile] = filecount[afile] + 1
			else:
				filecount[afile] = 1

print("Total warnings in all files = " + str(total))
print ("Warnings:   File:")
for key in filecount.keys(): 
	print(str(filecount[key]).rjust(9) + "   " + key)