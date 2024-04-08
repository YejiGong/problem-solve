import java.lang.Math;
import java.util.*;
class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        int num = times.length; //심사대 개수
        long maxTimes = (long)Arrays.stream(times).max().getAsInt();
        long left=0; long right=maxTimes*n; long mid = 0;
        while(left<=right){
            mid = (left+right)/2; //각 심사대가 갖고가는 시간의 수
            long complete = 0;
            for(int i=0; i<num; i++){
                complete += mid/times[i];
            }
            if(complete<n){
                left = mid+1;
            }
            else{
                right = mid-1;
                answer = mid;
            }
            
        }
        return answer;
    }
}