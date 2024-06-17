import java.util.*;
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] dp = new boolean[s.length()];
        Arrays.fill(dp, false);
        HashMap<String, Integer> maps = new HashMap<>();
        for(int i=0; i<wordDict.size(); i++){
            maps.put(wordDict.get(i),0);
        }

        for(int i=1; i<=s.length(); i++){
            if(maps.containsKey(s.substring(0,i))){
                dp[i-1]=true;
            }else{
                for(int j=0; j<i; j++){
                    if((j==0 || dp[j-1]==true) && maps.containsKey(s.substring(j,i))){
                        dp[i-1] = true;
                    }
                }
            }
        }
        return dp[s.length()-1];
    }
    
}