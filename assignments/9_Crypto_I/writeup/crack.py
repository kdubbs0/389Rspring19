#!/usr/bin/env python3

import hashlib
import string

def crack():
    hashes = 'hashes.txt' # open and read hashes.txt
    passwords = 'passwords.txt' # open and read passwords.txt
    characters = string.ascii_lowercase
    chars = []

    for line in open(passwords):
	for char in characters:
	    chars.append((char + line).rstrip())

    for char in chars:
	hashed = hashlib.sha256(char.rstrip().encode().rstrip()).hexdigest().rstrip()

	for line in open(hashes, 'r'):
	    if line.rstrip() == hashed:
		print(char + '\t:\t' + hashed)

#    for c in characters:
#        for p in passwords:
            # crack hashes

            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52

if __name__ == "__main__":
    crack()
