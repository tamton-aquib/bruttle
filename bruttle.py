#!/usr/bin/env python3
import pikepdf, zipfile
import sys, time
from hashlib import md5,sha1,sha224,sha256,sha384,sha512
# NOTE: these functions were taken from https://github.com/taj0023 (which is me btw)

R, G, B, E = "\033[31m", "\033[32m", "\033[36m", "\033[0m"

def ettup():
	for passwd in passlist:
		try:
			with pikepdf.open(filename, password = passwd) as pdfile:
				pdfile.save('output.pdf')
				print(f"{G}--------------------------------------------")
				print("          Found Password: -->  "+ passwd)
				print("--------------------------------------------")
				return

		except pikepdf._qpdf.PasswordError:
			print(f"{R}trying: {passwd}")

def ettuh():
	hashes = {"64": sha256, "32": md5, "128":sha512, "40": sha1, "96":sha384, "56": sha224}
	for line in lines:
		enc_wrd = line.encode()
		hash_type = hashes.get(str(len(filename)), "Nil")

		if hash_type == "Nil":
			print(f"{R}Hashtype not included in md5, sha1, sha224, sha256, sha384, sha512{E}")
			return

		digest = hash_type(enc_wrd).hexdigest().lower()

		if digest == filename:
			print(f"{G}---------------------------------------------------")
			print(f"         Password Found! --> {line}               ")
			print(f"---------------------------------------------------{E}")
			break
		else:
			print(f"{R}trying : {line}")

def ettuz():
	for password in lines:
		try:
			with zipfile.ZipFile(file=filename) as my_zip:
				my_zip.extractall('extracted', pwd=bytes(password.encode('utf-8').strip()))
				print(f"{G}-----------------------------------------------")
				print("       Password Found: --> " + password)
				print("-----------------------------------------------")
				return
		except:
			print(f'{R}trying: ' + password)
			time.sleep(0.0001)

def log(): print(f"Usage: python3 ettu_tools.py (zip|hash|pdf) filename/hash dictionary\n")

if __name__ == "__main__":
	if len(sys.argv) < 3: log(); sys.exit()
	option, filename, passlist = sys.argv[1:]

	with open(passlist,'r') as f:
		lines = [password for password in f.read().split('\n') if password]

	{"zip": ettuz, "hash": ettuh, "pdf": ettup}.get(option, log)()
