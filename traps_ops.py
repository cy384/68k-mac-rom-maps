# input: traps.txt with all lines of the format "_SwapMMUMode A05D"
# generate with something like:
# grep "0xA" Traps.h | awk '{print $1, $3}' | sed "s/,//" > traps.txt
# output: prints lines to include in ghidra 68000.sinc
# e.g.
#:SwapMMUMode is opbig=0xa0 & op37=11 & op02=5 { }

pairs = []
with open("traps.txt") as f:
	for line in f:
		name, val = line.strip().split(" ")
		front = (int(val,16) & 0xff00) >> 8
		back = int(val, 16) & 0x00ff
		name = name.replace("_","")

		a = (back & 0b11111000) >> 3
		b = (back & 0b00000111)
		
		# skip duplicates
		# yeah this is asympototically bad but n is small
		ok = True
		for p in pairs:
			if p[0] == hex(front) and p[1] == str(a) and p[2] == str(b):
				ok = False
		if ok:
			pairs.append((hex(front),str(a),str(b),name))

pairs.sort()

for (front,a,b,name) in pairs:
	spaces = " " * (30 - len(name))
	print(":"+name+spaces+"is opbig="+front+" & op37="+a+" & op02="+b+"\t\t\t{ }")
