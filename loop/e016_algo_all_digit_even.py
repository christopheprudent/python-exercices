start = 100
stop = 400
numbers = range(start, stop +1)
numbers_as_str = map(str, numbers)
all_digit_even = filter(lambda s : all([int(c) % 2 == 0 for c in s]), numbers_as_str)

print(','.join(all_digit_even))
