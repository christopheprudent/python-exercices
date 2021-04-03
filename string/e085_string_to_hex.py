def convert_bytearray_to_hex(ba):
	return ''.join([ hex(i)[2:] for i in ba ])

# web solution
def bytearray_to_hexadecimal(list_val):
     return ''.join('{:02x}'.format(x) for x in list_val)

list_val = [111, 12, 45, 67, 109] 
print("Original Bytearray :")
print(list_val)
print("\nHexadecimal string:")
print(convert_bytearray_to_hex(list_val))
print(bytearray_to_hexadecimal(list_val))
