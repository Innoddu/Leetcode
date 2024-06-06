def twoSum(nums, target):
	
	hashmap = {}
	index_1 = 0
	index_2 = 0

	for i, n in enumerate(nums):
		key = target - n
		if key in hashmap:
			index_1 = hashmap.get(key)
			index_2 = i
		else:
			hashmap[n] = i

	return [index_1, index_2]
