def encrypt_caesar(s, ofs=3):
	return ''.join([ chr(ord(c) - ofs) for c in s ])

def decrypt_caesar(s, ofs=3):
	return ''.join([ chr(ord(c) + ofs) for c in s ])

ec = encrypt_caesar('Julius Caesar l\'a utilisé pour sa correspondance privée')
print(ec)
print(decrypt_caesar(ec))
