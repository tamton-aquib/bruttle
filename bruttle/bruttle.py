#!/usr/bin/env python3
import pikepdf, zipfile
import sys, time
from tqdm import tqdm
from hashlib import md5, sha1, sha224, sha256, sha384, sha512
from os import path

R, G, B, E = "\033[31m", "\033[32m", "\033[36m", "\033[0m"

def prettify(s):
    print(f"{G}{'-'*45}\n{' '*10}Found Password: -->  {s}\n{'-'*45}{E}")

def ettup(target, lines):
    with tqdm(total=len(lines), colour="#986fec") as bar:
        bar.set_description(" Bruteforcing")
        for password in lines:
            try:
                with pikepdf.open(target, password=password) as pdfile:
                    pdfile.save('output.pdf')
                    bar.close()
                    prettify(password)
                    return

            except pikepdf.PasswordError:
                bar.update()

def ettuh(target, lines):
    hashes = { "64": sha256, "32": md5, "128":sha512, "40": sha1, "96":sha384, "56": sha224 }

    with tqdm(total=len(lines), colour="#986fec") as bar:
        bar.set_description(" Bruteforcing")
        for password in lines:
            hash_type = hashes.get(str(len(target)), None)

            if not hash_type:
                print(f"{R}Hashtype not included in md5, sha1, sha224, sha256, sha384, sha512{E}")
                return

            digest = hash_type(password.encode()).hexdigest().lower()
            prettify(password) if digest == target else bar.update()

def ettuz(target, lines):
    with tqdm(total=len(lines), colour="#986fec") as bar:
        bar.set_description(" Bruteforcing")
        for password in lines:
            try:
                with zipfile.ZipFile(file=target) as my_zip:
                    my_zip.extractall('extracted', pwd=bytes(password.encode().strip()))
                    bar.close()
                    prettify(password)
                    return
            except:
                time.sleep(0.0001)
                bar.update()

def log(*_): print(f"\n{G}Usage: bruttle <file/hash> <password_list>{E}\n")

def main():
    if len(sys.argv) < 3 or '-h' in sys.argv: log("", ""); sys.exit()
    target, passlist = sys.argv[1:]
    _, extension = path.splitext(target)

    with open(passlist) as f:
        lines = [password for password in f.read().split('\n') if password]

    { ".zip": ettuz, "": ettuh, ".pdf": ettup }.get(extension, log)(target, lines)

if __name__ == "__main__":
    main()
