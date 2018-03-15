#!/usr/bin/env python2

import sys
import struct
import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)

# Some constants. You shouldn't need to change these.
MAGIC = 0xbefedade
VERSION = 1
PNGMAGIC = "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a"


if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.rcff ")

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

def main():
	print(" ------- HEADER ------- ")
	print(" MAGIC: %s" % hex(magic))
	print(" VERSION: %d" % int(version))

	# We've parsed the magic and version out for you, but you're responsible for
	# the rest of the header and the actual RCFF body. Good luck!
	print(" TIMESTAMP: " +  datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S'))
	print(" AUTHOR: %s" % author)
	print(" SECTION_COUNT: %d" % section_count)

	print("-------  BODY  ------- ")

	start = 24 # I know that since the header is 24 bytes I need to start there
	end = start + 8 # first 8 bytes will include section type and length
	extra_secionts = 2 # start at 0 and increment until it crashes to get the real number
	for i in  range(section_count + extra_secionts):
		section_type, section_length = struct.unpack("<LL", data[start:end])
		section_number = i + 1
		if(section_length < 0):
			bork("length less than ZERO")
		print(" SECTION NUMBER: %d" % section_number)
		print(" SECTION_TYPE: %d" % section_type)
		print(" SECTION_LENGTH: %d" % section_length)

		start_of_section = end
		end_of_section = start_of_section + section_length
		print(" START BYTE: %d " %start_of_section)
		print(" END BYTE: %d " %end_of_section)
		
		if section_type == 1:
			print(" SECTION_ASCII ")
			contents = struct.unpack(str(section_length) + "s", data[start_of_section:end_of_section])
			print(" CONTENTS: %s\n" % contents)
		elif section_type == 2:
			print(" SECTION_UTF8 ")
			contents = struct.unpack(str(section_length) + "s", data[start_of_section:end_of_section])
			print(" CONTENTS: %s\n" % contents)
		elif section_type == 3:
			print(" SECTION_WORDS ")
			if(0 != section_length % 4):
				bork("section length error != mod 4")
			contents = struct.unpack("<%dL" % (section_length/4), data[start_of_section:end_of_section])
			print(" CONTENTS: %s\n" % unicode(contents))
		elif section_type == 4:
			print(" SECTION_DWORDS ")
			if(0 != section_length % 8):
				bork("section length error != mod 8")
			contents = struct.unpack("<%dQ" % (section_length/8), data[start_of_section:end_of_section])
			print(" CONTENTS: ")
			for i in range (section_length / 8):
				print(contents[i])
			print("\n")
		elif section_type == 5:
			print(" SECTION_DOUBLES ")
			if(0 != section_length % 8):
				bork("section length error != mod 8")
			contents = struct.unpack(str(section_length) + "s", data[start_of_section:end_of_section])
			print(" CONTENTS: %s\n" % contents)
		elif section_type == 6:
			print(" SECTION_COORD ")
			if(16 != section_length):
				bork("section length error != 16")
			cord_1 , cord_2 = struct.unpack("<dd", data[start_of_section:end_of_section])
			print(" CONTENTS: %s , %s \n" %(str(cord_1), str(cord_2)))
		elif section_type == 7:
			print(" SECTION_REFERENCE ")
			if(4 !=section_length):
				bork("error bad section length != 4")
			contents, = struct.unpack("<L", data[start_of_section:end_of_section])
			if(-1 > contents or contents > section_count):
				print(contents)
				bork("-1 or over max error on sections...")
			print(" CONTENTS: %s\n" % contents)
		elif section_type == 8:
			print(" SECTION_PNG ")
			contents =  data[start_of_section:end_of_section]
			pngFile = PNGMAGIC + contents #hex header for png file
			outFile = open(str(section_number) +"_output.png", "wb") #write binary for windows machines
			outFile.write(pngFile)
			outFile.close()
			
		else:
			print(" ERROR ")
			sys.exit()
				
		#setting up the start and end of the section header for the next iteration of the loop
		start = end_of_section 
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