import os
from cryptography.fernet import Fernet
files = []
for file in os.listdir():
	if file == "ransomware.py" or file == "thekey.key" or file =="decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)
with open ("thekey.key","rb") as key:
	secretkey=key.read()
for file in files :
	with open(file,"rb") as f:
		contents=f.read()
	content_decrypted=Fernet(secretkey).decrypt(contents)
	with open(file,"wb") as f:
		f.write(content_decrypted)

