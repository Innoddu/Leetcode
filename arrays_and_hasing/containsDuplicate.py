def hasDuplicate(self, nums: List[int]) -> bool:
        listSet = set()

        for n in nums:
            if n in listSet:
                return True
            else:
                listSet.add(n)
        return False
