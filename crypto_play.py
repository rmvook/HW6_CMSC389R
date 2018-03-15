import sys

'''
This code is used to generate key.txt so that the PNG magic could be obfuscated. This does not really add much, but was more of a curiosity.
'''

src = "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a"
key = "jetfule can't melt dank memes"
xorWord = lambda ss,cc: ''.join(chr(ord(s)^ord(c)) for s,c in zip(ss,cc*100))



encrypt = xorWord(src, key)
print encrypt
f = open("key.txt", 'w')
f.write(encrypt)
f.close()

decrypt = xorWord(encrypt,key)
print decrypt

f = open("key.txt", 'r')
xor =  f.read().replace('\n', '')

decrypt = xorWord(xor,key)

print(decrypt)
f.close()
