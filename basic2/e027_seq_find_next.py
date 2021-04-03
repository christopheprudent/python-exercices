def seq_find_next(seq):
	if len(seq) < 3:
		raise ValueError

	# arithmetic progression (AP) : seq(i+1) = seq(i) + constant
	if seq[1] - seq[0] == seq[2] - seq[1]:
		_diff = seq[1] - seq[0]
		return seq[-1] + _diff
	else:
		# geometric progression (GP) : seq(i+1) = seq(i) * constant
		if seq[1] / seq[0] == seq[2] / seq[1]:
			_ratio = seq[1] // seq[0]
			return seq[-1] * _ratio

print(seq_find_next([3, 5, 7, 9, 11, 13]))
print(seq_find_next([2, 6, 18, 54]))
		
