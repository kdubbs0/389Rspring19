#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():
    hashes = 'hashes.txt' # open and read hashes.txt
    passwords = 'passwords.txt' # open and read passwords.txt
    characters = string.ascii_lowercase
    server_ip = '134.209.128.58'
    server_port = 1337
    chars = []
    hash_list = {}
    count = 0

    for line in open(passwords):
	for char in characters:
	    chars.append((char + line).rstrip())

    for char in chars:
	hash_list[hashlib.sha256(char.rstrip().encode().rstrip()).hexdigest().rstrip()] = char

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))

    # parse data
    # crack 3 times
    while count < 4:
	data = s.recv(1024).decode()
	s.send((hash_list[data.rstrip()[len(data) - 69 : len(data) - 4].rstrip()] + "\n").encode())
	count += 1
	if count == 3:
	    print(s.recv(1024).decode().rstrip())
	    break

if __name__ == "__main__":
    server_crack()
