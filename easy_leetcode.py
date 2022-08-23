# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = (len(nums))
        for i in range(length):
            for j in range(length):
                if i == j:
                    j+=1
                val = nums[i] + nums[j]
                if val == target:
                    new_lst = [i,j]
                    return new_lst



# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.
 
# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
# Constraints:
# -231 <= x <= 231 - 1

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    temp = x
    reverse = 0
    while x:
        last = x % 10
        reverse = reverse * 10 + last
        x = x // 10
    return reverse == temp



# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        val = 0
        temp = [c for c in s]
        i = 0
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for ch in s:
            for s in dic.keys():
                if ch == s:
                    if i == 0:
                        val += dic[s]
                        break
                    if dic[s] == 5 and temp[i-1]=='I':  
                        val += 3
                        break
                    elif dic[s] == 10 and temp[i-1]=='I':
                        val += 8
                        break
                    elif dic[s] == 50 and temp[i-1]=='X':
                        val += 30    
                        break
                    elif dic[s] == 100 and temp[i-1]=='X':
                        val += 80
                        break
                    elif dic[s] == 500 and temp[i-1]=='C':
                        val += 300
                        break
                    elif dic[s] == 1000 and temp[i-1]=='C':
                        val += 800
                        break
                    else:
                        val += dic[s]
            i+=1
        return val


  
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""

# Explanation: There is no common prefix among the input strings.
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    temp = []
    if len(strs) == 1:
            return strs[0]
    i = 0
    if strs[i] == "":
        return ""
    else:
        x = [s for s in (strs[i])]

    for c in strs[1:]:
        for i in range(len(c)):
            if len(c) > len(x):
                x.append("")
            if x[i] == c[i]:
                temp += c[i]
            else:
                break
        x = [s for s in (temp)]
        temp = []
        if x == []:
                break

    result = "".join(map(str, x))
    return result
