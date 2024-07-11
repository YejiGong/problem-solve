import java.io.*;
import java.util.*;
import java.lang.Math;

public class Main {
    public static int[] nums;
    public static int N;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        nums = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++){
            nums[i] = Integer.parseInt(st.nextToken());
        }
        int idx = 0;
        int result = 0;
        while(idx<N){
            result += getSequenceNum(idx);
            if(nums[idx]==0){
                idx++;
            }
        }
        System.out.println(result);
    }

    public static int getSequenceNum(int n){
        if(nums[n]==0){
            return 0;
        }
        int length = 0;
        int idx = n;
        int minimumVal = Integer.MAX_VALUE;
        while(idx<N && length<3 && nums[idx]>0){
            minimumVal = Math.min(minimumVal, nums[idx]);
            length++;
            idx++;
        }
        if(length==3 && nums[n+1]!=minimumVal){
            if((nums[n+1]>nums[n+2])){
                length--;
                idx--;
                minimumVal = Math.min(nums[n+1]-nums[n+2], minimumVal);
            }
        }
        for(int i=n; i<idx; i++){
            nums[i] -= minimumVal;
        }
        int result = 0;
        if(length==1){
            return minimumVal*3;
        }else if(length==2){
            return minimumVal*5;
        }else if(length==3){
            return minimumVal*7;
        }else{
            return 0;
        }
    }


}

