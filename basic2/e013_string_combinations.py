import itertools

string_maps = {
"1": "abc",
"2": "def",
"3": "ghi",
"4": "jkl",
"5": "mno",
"6": "pqrs",
"7": "tuv",
"8": "wxy",
"9": "z"
}

list_of_combinations = list()
for v in string_maps.values():
	list_of_combinations += list(itertools.combinations(v, 2))

print(list_of_combinations) 
