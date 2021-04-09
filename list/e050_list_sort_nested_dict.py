# web solution
my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
print("Original List: ")
print(my_list)
my_list.sort(key=lambda e: e['key']['subkey'], reverse=True)
print("reversed sorted List (on subkey): ")
print(my_list)

#my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
my_list = [{'key': {'subkey': '1'}}, {'key': {'subkey': '10'}}, {'key': {'subkey': '5'}}]
print("Original List: ")
print(my_list)
#my_list.sort(key=lambda e: e['key']['subkey'], reverse=True)
my_list.sort(key=lambda e: int(e['key']['subkey']), reverse=True)
print("reversed sorted List (on subkey): ")
print(my_list)
