
def test(nums):
    hashmap = {}
    res = []
    for n in nums:
        hashmap[n] = hashmap.get(n, 0) + 1 
    
    for n in nums:
        if n * 2 in hashmap:
            if hashmap.get(n*2) == 1:
                res.append(n)
    print(hashmap)
    return res

lst = [1,2,3,4,5,6,7,8, 9, 0,8]
lst2 = [7,17,11,1,23]
lst3 = [1,1,2]
print(test(lst))
print(test(lst2))
print(test(lst3))