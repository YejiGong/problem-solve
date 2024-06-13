class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        tmp_nums1 = nums1[:m]
        tmp_nums2 = nums2[:n]
        tmp_nums1.sort()
        tmp_nums2.sort()
        res = []
        f_idx = 0
        s_idx = 0
        while f_idx<m and s_idx<n:
            if tmp_nums1[f_idx]<tmp_nums2[s_idx]:
                res.append(tmp_nums1[f_idx])
                f_idx+=1
            elif tmp_nums1[f_idx]>tmp_nums2[s_idx]:
                res.append(tmp_nums2[s_idx])
                s_idx+=1
            else:
                res.append(tmp_nums1[f_idx])
                res.append(tmp_nums2[s_idx])
                f_idx+=1
                s_idx+=1
        if f_idx<m:
            for i in range(f_idx,m):
                res.append(tmp_nums1[i])
        if s_idx<n:
            for i in range(s_idx,n):
                res.append(tmp_nums2[i])
        for i in range(n+m):
            nums1[i] = res[i]
        
