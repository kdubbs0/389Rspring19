#!/usr/bin/env python2

import sys
import struct
from datetime import datetime


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version, timestamp, author, nsects = struct.unpack("<LLL8sL", data[0:24])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %s" % datetime.utcfromtimestamp(int(timestamp)).strftime("%Y-%m-%d %H:%M:%S"))
print("AUTHOR: %s" % str(author))
print("SECTION COUNT: %d" % int(nsects))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
start = 24
end = start + 8
for x in range (0, int(nsects)):
    stype, slen = struct.unpack("<LL", data[start:end])
    print("SECTION TYPE: %s" % hex(stype))
    print("SECTION LENGTH: %d" % int(slen))
    start = end
    end = start + int(slen)
    if int(slen) > 0:
	if hex(stype) == "0x3":
	    svalue = str(struct.unpack("<{}L".format(slen/4), data[start:end]))[2:-3]
	    print("SECTION VALUE: %s" % str(svalue))
	elif hex(stype) == "0x4":
	    svalue = str(struct.unpack("<{}LL".format(slen/8), data[start:end]))[2:-3]
	    print("SECTION VALUE: %s" % str(svalue))
	elif hex(stype) == "0x5":
	    svalue = str(struct.unpack("<{}Q".format(slen/8), data[start:end]))[2:-3]
	    print("SECTION VALUE: %s" % str(svalue))
	elif hex(stype) == "0x6":
	    if int(slen) == 16:
		svalue1 = str(struct.unpack("<{}Q".format(1), data[start:start+8]))[2:-3]
		svalue2 = str(struct.unpack("<{}Q".format(1), data[end-8:end]))[2:-3]
		print("SECTION VALUE: ({},{})".format(svalue1, svalue2))
	    else:
		bork("Bad size! Got %s, expected 16" % int(slen))
	elif hex(stype) == "0x7":
	    if int(slen) == 4:
		svalue = str(struct.unpack("<{}s".format(slen), data[start:end]))[2:-3]
		print("SECTION VALUE: %s" % str(svalue))
	    else:
		bork("Bad size! Got %s, expected 4" % int(slen))
	elif hex(stype) == "0x8":
	    svalue = "\\x89\\50\\4E\\47\\0D\\0A\\1A\\0A" + str(struct.unpack("<{}s".format(slen), data[start:end]))[2:-3]
	    print("SECTION VALUE: %s" % str(svalue))
	    file = open("section{}d.png".format(x), "w")
	    file.write(svalue)
	    file.close()
	elif hex(stype) == "0x9":
	    svalue = "\\G\\I\\F\\8\\7\\a" + str(struct.unpack("<{}s".format(slen), data[start:end]))[2:-3]
	    print("SECTION VALUE: %s" % str(svalue))
	    file = open("section{}d.gif".format(x), "w")
	    file.write(svalue)
	    file.close()
	elif hex(stype) == "0xA":
	    svalue = "\\G\\I\\F\\8\\9\\a" + str(struct.unpack("<{}s".format(slen), data[start:end]))[2:-3]
            print("SECTION VALUE: %s" % str(svalue))
            file = open("section{}d.gif".format(x), "w")
            file.write(svalue)
            file.close()
	elif hex(stype) == "0x1" or hex(stype) == "0x2":
            svalue = struct.unpack("<{}s".format(slen), data[start:end])
	    print("SECTION VALUE: %s" % str(svalue)[2:-3])
	else:
	    bork("Bad type! Got %s" % hex(stype))
        start = end
        end = start + 8
