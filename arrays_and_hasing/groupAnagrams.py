def groupAnagrams(strs):
        sorted_list = []
        hashmap = {}

        for i, s in enumerate(strs):
            char_list = list(s)
            char_list.sort()
            sorted_string = ''.join(char_list)
            sorted_list.append(char_list)
            if sorted_string not in hashmap:
                hashmap[sorted_string] = []
                hashmap[sorted_string].append(i)
            else:
                hashmap[sorted_string].append(i)
 
        res = []
        return_list = []
        idx = 0
        for key in hashmap:
            size = len(hashmap.get(key))
            while idx < size:
                res.append(strs[hashmap.get(key)[idx]])
                idx += 1

            return_list.append(res)
            res = []
            idx = 0


        return return_list
