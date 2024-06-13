def maxArea(heights):

        maxHeight = 0
        distance = 0 
        left = 0
        right = len(heights) - 1
        while left < right:
            
            distance = abs(left - right)
            if heights[left] < heights[right]:
                maxHeight = max(heights[left] * distance, maxHeight)
                left += 1
            elif heights[left] > heights[right]:
                maxHeight = max(heights[right] *  distance, maxHeight)
                right -= 1
            else:
                maxHeight = max(heights[right] *  distance, maxHeight)
                right -= 1
      

        return maxHeight
   
