def topKFrequent(nums, k):
        hashmap = {}
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 0
            else:
                hashmap[n] += 1
        sorted_by_value = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))

        res = []
        keys = list(sorted_by_value.keys())

        for i in range(k):
            res.append(keys[i])


        return res


