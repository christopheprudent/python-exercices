def all_3items_target_sum(list, target_sum):
	if len(list) < 3:
		return False

	tuples = ()
	for i, vi in enumerate(list):
		for j, vj in enumerate(list):
			if i == j:
				continue
			for k, vk in enumerate(list):
				if k == i or k == j:
					continue

				if vi + vj + vk == target_sum:
					tuples += (i, j, k),


	if len(tuples) > 0:
		print(list, 'solutions: ', tuples)
		return True

	return False

all_3items_target_sum([10, 20, 20, 20], 70)
all_3items_target_sum([10, 20, 30, 40], 70)
all_3items_target_sum([10, 30, 40, 20], 70)

