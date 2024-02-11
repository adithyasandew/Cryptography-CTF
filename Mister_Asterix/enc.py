# Flag Format - H4ckK4P(<PlainText>)

from TheSpy import secret

def encrypt(txt,s):
	enc_txt = ""
	for i in range(len(txt)):
		char = txt[i]
		if (char.isupper()):
			enc_txt += chr((ord(char) + s - 65) % 26 + 65)
		else:
			enc_txt += chr((ord(char) + s - 97) % 26 + 97)
	return enc_txt

s = 4
with open("cipher", "w") as cipher:
    cipher.write(encrypt(secret,s))
