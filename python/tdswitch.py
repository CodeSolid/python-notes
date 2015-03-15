import os
import re
from sys import argv, exit
if len(argv) != 2:
	s = """Usage:  python tdswitch <base td directory>"""	
	print(s)
	exit()

dircur = os.getcwd()
pattern = re.compile(r"C:\\td\\.*?\\(?P<remainder>.*)")
m = pattern.search(dircur)
tail = m.group("remainder")
head = argv[1]
wholepath = head + "\\" + tail
with open("C:\\apps\\batch\\tdswitch.bat", "w") as f:
	f.write("pushd " + wholepath)
