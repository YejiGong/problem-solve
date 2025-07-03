score = [(i, int(input())) for i in range(8)]
score.sort(reverse=True, key = lambda x:x[1])
print(sum([i[1] for i in score[:5]]))

nums = [i[0] for i in score[:5]]
nums.sort()
print(' '.join([str(i+1) for i in nums]))