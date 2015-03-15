import sys

if len(sys.argv) != 2:
	print("Usage:  python dumpfile <FILENAME>")
	sys.exit()

filename = sys.argv[1]

with open(filename, 'r') as lines:
	for l in lines:
		chars = list(l)
		for c in chars:
			if(c == '\t'):
				sys.stdout.write("  ")
			else:
				sys.stdout.write(c)


		# sys.stdout.write(l)
		# print(l.rstrip())
