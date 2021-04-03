int_val = 2 ** 64 -1
print(int_val.bit_length())

if int_val.bit_length() <= 63:
    print((-2 ** 63).bit_length())
    print((2 ** 63).bit_length())
	
