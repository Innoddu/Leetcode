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






def isValid(s):
    """
    :type s: str
    :rtype: bool
    input
    ()[]{}
    """
    dic = {"(":")","[":"]","{":"}"}
    stack = []
    open_bracket = ['(', '[', '{']
    close_bracket = [')', ']', '}']

    for i in s:
        if i in open_bracket:
            stack.append(i)
        elif i in close_bracket:
            if not stack or dic[stack.pop()] != i:
                return False
    return len(stack) == 0
        


# DP 
def climbStairs(n):
    """
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    lst = [0] * (n + 1)
    lst[1] = 1
    lst[2] = 2
    for i in range(3, n+1):
        lst[i] =  lst[i - 1] + lst[i - 2]
    return lst[n]



def mySqrt(x):
    """
    Given a non-negative integer x, 
    return the square root of x rounded down to the nearest integer.
    The returned integer should be non-negative as well.

    You must not use any built-in exponent function or operator.
    """
    if x == 1 or x == 3:
        return 1
    root_val = x**(1/2)
    # print(root_val)
    if x % 2 != 0:
        val = root_val // 1
        return int(val)
    else:
        return int(root_val)



def maxArea(height):
    """
    11. Container With Most Water
    Medium
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, such that the container contains the most water.
    Return the maximum amount of water a container can store.
    Notice that you may not slant the container.
    """
    left = 0
    right = len(height) - 1
    max_area = []
    
    while left < right:
        if height[left] < height[right]:
            max_area.append(height[left] * (right-left))
            left += 1
        else:
            max_area.append(height[right] * (right-left))
            right -= 1
    return max(max_area)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def deleteDuplicates(head):
    """
    83. Remove Duplicates from Sorted List
    Easy.
    Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
    Return the linked list sorted as well.
    """
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head



def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    88. Merge Sorted Array
    Easy

    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

    Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
    
    To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

    """
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] <= nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
        elif nums1[p1] >= nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
            p -= 1
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1





def inorderTraversal(root):
    """
    94. Binary Tree Inorder Traversal
    Easy

    Given the root of a binary tree, return the inorder traversal of its nodes' values.
    """
    result = []
    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

    inorder(root)
    return result


def isSameTree(p, q):
    """
    100. Same Tree
    Easy

    Given the roots of two binary trees p and q, write a function to check if they are the same or not.

    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
    """
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)




def generate(numRows):
    """
    118. Pascal's Triangle
    Easy

    Given an integer numRows, return the first numRows of Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly above it as
    """
    t = []

    for i in range(numRows):
        row = [1] * (i + 1)  # Initialize the row with 1s

        # Calculate values from the second element to the second-to-last element
        for j in range(1, i):
            row[j] = t[i - 1][j - 1] + t[i - 1][j]

        t.append(row)

    return t



def isSymmetric(root):
    """
    101. Symmetric Tree
    Easy

    Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
    """
    if not root:
        return True
    return subchildCheck(root.left, root.right)

def subchildCheck(left, right):
    if not left and not right:
        return True

    if not left or not right or left.val != right.val:
        return False

    return subchildCheck(left.left, right.right) and subchildCheck(left.right, right.left)





def maxDepth(root):
    """
    104. Maximum Depth of Binary Tree
    Easy

    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    """
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    return max(left_depth, right_depth) + 1


def sortedArrayToBST(nums):
    """
    108. Convert Sorted Array to Binary Search Tree
    Easy

    Given an integer array nums where the elements are sorted in ascending order, convert it to a 
    height-balanced binary search tree.
    """
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])

    left_nums = nums[:mid]
    right_nums = nums[mid+1:]

    root.left = sortedArrayToBST(left_nums)
    root.right = sortedArrayToBST(right_nums)

    return root






def isBalanced(root):
    """
    110. Balanced Binary Tree
    Easy

    Given a binary tree, determine if it is height-balanced.
    """
    if not root:
        return True

    def height(node):
        if not node:
            return 0

        left_height = height(node.left)
        right_height = height(node.right)

        return max(left_height, right_height) + 1

    left_height = height(root.left)
    right_height = height(root.right)

    if abs(left_height - right_height) > 1:
        return False

    return isBalanced(root.left) and isBalanced(root.right)



def minDepth(root):
    """
    111. Minimum Depth of Binary Tree
    Easy

    Given a binary tree, find its minimum depth.

    The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

    Note: A leaf is a node with no children.
    """
    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    if not root.left:
        return minDepth( root.right) + 1

    if not root.right:
        return minDepth(root.left) + 1

    return min(minDepth(root.left), minDepth(root.right)) + 1



def hasPathSum(root, targetSum):
    """
    112. Path Sum
    Easy
    
    Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

    A leaf is a node with no children.
    """
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == targetSum

    remaining_sum = targetSum - root.val

    return hasPathSum(root.left, remaining_sum) or hasPathSum(root.right, remaining_sum)







