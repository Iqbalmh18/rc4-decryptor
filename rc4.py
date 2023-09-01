#!/usr/bin/env python3
import os

# default hardcoded key
key = b'21983453453435435738912738921'

def rc4_decrypt(key, ciphertext):
    S = list(range(256))
    j = 0
    out = []
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    i = j = 0
    for byte in ciphertext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(byte ^ S[(S[i] + S[j]) % 256])
    return bytes(out)

def __rc4__():
    print(f'''
   ___  _________   ___                        __
  / _ \/ ___/ / /  / _ \___ __________ _____  / /____  ____
 / , _/ /__/_  _/ / // / -_) __/ __/ // / _ \/ __/ _ \/ __/
/_/|_|\___/ /_/  /____/\__/\__/_/  \_, / .__/\__/\___/_/
                                  /___/_/

Python program to decrypt encrypted files with extension ".coderCrypt"
from  Ransomware "CyberPunk 2077" using Key Scheduling Algorithm (KSA)
and Pseudo-Random Generation Algorithm (PRGA).

[-] using default hardcoded key "{key.decode()}"
[-] example path for android "/sdcard"''')
    path_encrypted = str(input('[?] input path: '))
    if not os.path.isdir(path_encrypted): exit('[!] path not found ...')
    file_encrypted = os.popen(f'find -O3 -L {path_encrypted} -name "*.coderCrypt"', 'r').read().splitlines()
    if len(file_encrypted) == 0: exit(f'[!] no encrypted file found on {path_encrypted} ...')
    print('')
    i = 0
    for file in file_encrypted:
        i += 1
        print(f'{str(i)} - decrypting files: {os.path.basename(file)} ... ')
        outp = file.replace('.coderCrypt', '')
        with open(file, 'rb') as f:
            ciphertext = f.read()
        plaintext = rc4_decrypt(key, ciphertext)
        with open(outp, 'wb') as f:
            f.write(plaintext)
        if os.path.isfile(outp): os.remove(file)
    print(f'''
[+] your files have been processed ...
[+] total {str(i)} files successfully decrypted !
    ''')

if __name__ == '__main__':
    try: __rc4__()
    except KeyboardInterrupt: exit(1)
