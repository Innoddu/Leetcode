class Solution:
   def encode(self, strs):

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        # if len(strs) == 0:
        #     return ""
        # if len(strs) == 1 and len(strs[0]) == 0:
        #     return " "
        # print(len(strs[0]))
        # print(len(strs))
        # self.hashmap = {}
        # self.lenghtOfList = len(strs)
        # self.lenString = deque()
        # self.lenString.append(len(strs[0]))

        # oneString = ""
        # encoded_strs = ""
        # res = []
        # idx = 0
        # valid_key = set()
        # flag = True
        
        # for i in range(1, len(strs)):
        #     self.lenString.append(self.lenString[i-1] + len(strs[i]))
        
        # for i in range(len(strs)):
        #     oneString += strs[i]


        # # Generate Random Character without duplicate
        # for i in range(len(oneString)):
        #         characters = string.ascii_letters + string.digits
        #         random_string = ''.join(random.sample(characters, 1))
        #         if random_string in valid_key:
        #             while flag:
        #                 random_string = ''.join(random.sample(characters, 1))
        #                 if random_string not in valid_key:
        #                     flag = False
        #             flag = True
        #         else:
        #             valid_key.add(random_string)
        #         print(random_string)
                
        #         self.hashmap[oneString[i]] = random_string
        
 
        
        # for c in strs:
        #     for i in range(len(c)):
        #         if c[i] in self.hashmap:
        #             encoded_strs += self.hashmap[c[i]]


        # return encoded_strs


    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
        

        # if s == " ":
        #     return [""]
        # if len(s) == 0:
        #     return []

        # decoded_strs = ""
        # res = []
        # idx = 0
        # prev_size = 0

        # while idx < self.lenghtOfList:
        #     size = self.lenString.popleft()
        #     for i in range(prev_size, size):
        #         for key, value in self.hashmap.items():
        #             if value == s[i]:
        #                 decoded_strs += key

        #     res.append(decoded_strs)
        #     decoded_strs = ""
        #     idx += 1
        #     prev_size = size

        # return res
