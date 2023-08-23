class Solution {
    int result = 0;
    public int solution(int[] numbers, int target) {
        dfs(numbers, 1, numbers[0]*(-1),target);
        dfs(numbers, 1, numbers[0],target);
        return result;
    }
    public void dfs(int[] n, int idx, int sum, int target){
        if(idx==n.length){
            if(sum==target){
                result+=1;
            }
        }else{
            dfs(n, idx+1, sum+n[idx], target);
            dfs(n, idx+1, sum-n[idx], target);
        }
    }
}