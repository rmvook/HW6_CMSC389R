#!/usr/bin/env python2

import sys
import struct
import datetime
print(
   
)

# cmsc389  63 6d 73 63 33 38 39
# CMSC389  43 4d 53 43 33 38 39

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0xbefedade
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.rcff")

# Normally we'd parse a stream to save memory, but the RCFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as rcff:
    data = rcff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version, timestamp, author, section_count = struct.unpack("<LLL8sL", data[0:24])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

#,  = struct.unpack("<LL", data[8:16])

def main():
	print("------- HEADER -------")
	print("MAGIC: %s" % hex(magic))
	print("VERSION: %d" % int(version))

	# We've parsed the magic and version out for you, but you're responsible for
	# the rest of the header and the actual RCFF body. Good luck!
	print("TIMESTAMP: " +  datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S'))
	print("AUTHOR: %s" % author)
	print("SECTION_COUNT: %d" % section_count)

	print("-------  BODY  -------")

	start = 24
	end = start + 8
	for i in  range(11):
		section_type, section_length = struct.unpack("<LL", data[start:end])

		print("SECTION_TYPE: %d" % section_type)
		print("SECTION_LENGTH: %d" % section_length)
		'''	
		SECTION_ASCII (0x1)
		SECTION_UTF8 (0x2) -- UTF-8-encoded text^3.
		SECTION_WORDS (0x3) -- Array of words.
		SECTION_DWORDS (0x4) -- Array of dwords.
		SECTION_DOUBLES (0x5) -- Array of doubles.
		SECTION_COORD (0x6) -- (Latitude, longitude) tuple of doubles.
		SECTION_REFERENCE (0x7) -- The index of another section.
		SECTION_PNG (0x8) -- Embedded PNG image.
		'''
		current = end + section_length


		if section_type == 1:
			print("SECTION_ASCII")
			args = str(section_length) + "s"
			contents , = struct.unpack(args, data[end:current])
			print("CONTENTS: %s\n" % contents)

		elif section_type == 2:
			print("SECTION_UTF8")
			args = str(section_length) + "s"
			contents , = struct.unpack(args, data[end:current])
			print("CONTENTS: %s\n" % contents)
		elif section_type == 3:
			print("SECTION_WORDS")
			args = str(section_length) + "s"
			contents , = struct.unpack(args, data[end:current])
			print("CONTENTS: %s\n" % unicode(contents))
		elif section_type == 4:
			print("SECTION_DWORDS")
			args = str(section_length) + "s"
			contents , = struct.unpack(args, data[end:current])
			print("CONTENTS: %s\n" % contents)
		elif section_type == 5:
			print("SECTION_DOUBLES")
			args = str(section_length) + "s"
			contents , = struct.unpack(args, data[end:current])
			print("CONTENTS: %s\n" % contents)
		elif section_type == 6:
			print("SECTION_COORD")
			args = str(section_length) + "s"
			contents , = struct.unpack(args, data[end:current])
			print("CONTENTS: %s\n" % contents)
		elif section_type == 7:
			print("SECTION_REFERENCE")
			args = str(section_length) + "s"
			contents , = struct.unpack(args, data[end:current])
			print("CONTENTS: %s\n" % contents)
		elif section_type == 8:
			print("SECTION_PNG")
		
		else:
			print("ERROR")
			sys.exit()
		


		

		start = current
		end = start + 8

if __name__ == "__main__":
	main()


'''
flags: Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9 converts in base 64 to utf-8 as 
CMSC389R-{h1dd3n-s3ct10n-1n-f1l3}

I used: https://www.base64decode.org/


NF2CO4ZANRUWWZJAMEQGMYLDORXXE6JMEBRHK5BAMZXXEIDGN5XWIIIK

was base32 for 

it's like a factory, but for food!


'''