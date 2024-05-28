# 435. Non-overlapping Intervals
def eraseOverlapIntervals( intervals ):
        intervals.sort(key=lambda i: i[0])
        endVal = intervals[0][1]
        cnt = 0
        for start, end in intervals[1:]:
            if endVal > start:
                cnt += 1
                endVal = min(end, endVal)
            else:
                endVal = end
                
        return cnt
