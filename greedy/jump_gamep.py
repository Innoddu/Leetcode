# 55. Jump Game
def canJump(nums):
        goal = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
                print(goal, i)
            
        return True if goal == 0 else False
