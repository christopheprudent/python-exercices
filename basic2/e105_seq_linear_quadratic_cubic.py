# 1st differences is linear
# https://courses.lumenlearning.com/waymakercollegealgebra/chapter/formulas-for-arithmetic-sequences/
def is_seq_linear(seq):
	n = len(seq)
	if n < 2:
		return (False, [])

	_r = seq[1] - seq[0]
	# seq(n) = seq(n-1) - r = seq(1) + r(n-1)

	return (all( j-i == _r for j, i in zip(seq[1:], seq)), [_r])
	
# 2nd differences is linear
# https://mathsmadeeasy.co.uk/gcse-maths-revision/quadratic-sequences-gcse-maths-revision-worksheets/
def is_seq_quadratic(seq):
	n = len(seq)
	if n < 2:
		return (False, [])

	diff_seq = [ seq[i+1] - seq[i] for i in range(n-1) ]
	diff_seq_linear, diff_seq_reason = is_seq_linear(diff_seq)
	if not diff_seq_linear:
		return (False, [])

	# un = a*n2 + b*n + c
	a = diff_seq_reason[0] // 2	

	n2 = [ i**2 for i in range(n) ]
	un_an2 = [ seq[i] - (a * n2[i]) for i in range(n) ]
	un_an2_linear, un_an2_reason = is_seq_linear(un_an2)
	if not un_an2_linear:
		return (False, [])

	b = un_an2_reason[0]
	c = seq[2] - a - (2**b)
	return (True, [a, b, c])


# 3rd differences is linear
# https://www.radfordmathematics.com/algebra/sequences-series/difference-method-sequences/cubic-sequences.html
def is_seq_cubic(seq):
	n = len(seq)
	if n < 2:
		return (False, [])

	diff_seq = [ seq[i+1] - seq[i] for i in range(n-1) ]
	#print('diff_seq={}'.format(diff_seq))
	diff2_seq = [ diff_seq[i+1] - diff_seq[i] for i in range(n-2) ]
	#print('diff2_seq={}'.format(diff2_seq))
	diff3_seq = [ diff2_seq[i+1] - diff2_seq[i] for i in range(n-3) ]
	#print('diff3_seq={}'.format(diff3_seq))

	diff3_seq_linear, diff3_seq_reason = is_seq_linear(diff3_seq)
	if not diff3_seq_linear:
		return (False, [])
	else:
		return (True, [diff3_seq_reason[0]])

# web solution
# sioux! reuse previous differences each time: 1st, 2nd, 3rd, ...
def Seq_Linear_Quadratic_Cubic(seq_nums):
  seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
  if len(set(seq_nums)) == 1: return "Linear Sequence"
  seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
  if len(set(seq_nums)) == 1: return "Quadratic Sequence"
  seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
  if len(set(seq_nums)) == 1: return "Cubic Sequence"

print(is_seq_linear([0,2,4,6,8,10]))
print(is_seq_quadratic([0,2,4,6,8,10]))
print(is_seq_cubic([0,2,4,6,8,10]))

print(is_seq_linear([1,4,9,16,25]))
print(is_seq_quadratic([1,4,9,16,25]))
print(is_seq_cubic([1,4,9,16,25]))

print(is_seq_linear([0,12,10,0,-12,-20]))
print(is_seq_quadratic([0,12,10,0,-12,-20]))
print(is_seq_cubic([0,12,10,0,-12,-20]))

print(is_seq_linear([1,2,3,4,5]))
print(is_seq_quadratic([1,2,3,4,5]))
print(is_seq_cubic([1,2,3,4,5]))
