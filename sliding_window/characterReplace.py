def characterReplacement(s, k):

        char_count = defaultdict(int)
        
        left = 0
        max_freq = 0
        max_length = 0
        
        for right in range(len(s)):
            char_count[s[right]] += 1
            max_freq = max(max_freq, char_count[s[right]])
            
            if (right - left + 1) - max_freq > k:
                char_count[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
