 # res用来存放结果
def permuteUnique2(nums):
        if not nums: return []
        res = []
        used = [0] * len(nums)
        def backtracking(used, path):
            # 终止条件
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    if i>0 and nums[i] == nums[i-1] and not used[i-1]:
                        continue
                    used[i] = 1
                    path.append(nums[i])
                    backtracking(used, path)
                    path.pop()
                    used[i] = 0
        # 记得给nums排序
        backtracking(used,[])
        print(res)
        return res

permuteUnique2([1,1,2])