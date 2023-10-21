#!/bin/python3

import hashlib,binascii 
import sys
try:
    hash = hashlib.new('md4', str(sys.argv[1]).encode('utf-16le')).digest() 
    print("aad3c435b514a4eeaad3b935b51304fe:"+str(binascii.hexlify(hash)).lstrip("b'").rstrip("'"))
except:
    print("You did not supply a value to hash!\nUsage: ntlmhash.py <PASS_TO_HASH>")
