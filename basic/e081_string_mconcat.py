def mconcat(*args):
	_result=''
	for s in args:
		_result+=s
	return _result

_s1= 'azerty'
print(mconcat('1234', 'abc', _s1))
