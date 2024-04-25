import java.util.*;
import java.lang.Math;
class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        int N = citations.length;
        int answer = 0;
        for(int i=0; i<N; i++){
            if(i>0 && citations[i-1]==citations[i]) continue;
            if(N-i<=citations[i]){
                answer = Math.max(answer,N-i);
            }
        }
        return answer;
    }
}