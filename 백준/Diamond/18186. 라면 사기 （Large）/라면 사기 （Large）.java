import java.io.*;
import java.util.*;
import java.lang.Math;

public class Main {
    public static int[] nums;
    public static int N;
    public static long B;
    public static long C;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        nums = new int[N];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++){
            nums[i] = Integer.parseInt(st.nextToken());
        }
        int idx = 0;
        long result = 0;

        while(idx<N){
            result += getSequenceNum(idx);
            if(nums[idx]==0){
                idx++;
            }
        }
        System.out.println(result);
    }

    //1 2 1
    //0 1 1 -> 0 0 0 : B+B+C = 2B+2C
    //0 1 0 -> 0 0 0 : B+2C+B = 2B+2C
    //0 2 1 -> 0 0 1 -> 0 0 0 = 4B -> 4B<2B+2C : 2B<2C : B<C
    public static long getSequenceNum(int n){
        if(nums[n]==0){
            return 0;
        }
        int length = 0;
        int idx = n;
        int minimumVal = Integer.MAX_VALUE;
        if(B>C) {
            while (idx < N && length < 3 && nums[idx] > 0) {
                minimumVal = Math.min(minimumVal, nums[idx]);
                length++;
                idx++;
            }

            if (length == 3 && nums[n + 1] != minimumVal) {
                if ((nums[n + 1] > nums[n + 2])) {
                    length--;
                    idx--;
                    minimumVal = Math.min(nums[n + 1] - nums[n + 2], minimumVal); //B+2C + B-> B+C + B +C .. => 2B+2C
                }
            }
        }else{
            length = 1 ;
            idx++;
            minimumVal = nums[n];
        }
        for(int i=n; i<idx; i++){
            nums[i] -= minimumVal;
        }
        if(length==1){
            return minimumVal*B;
        }else if(length==2){
            return minimumVal*(B+C);
        }else if(length==3){
            return minimumVal*(B+2*C);
        }else{
            return 0;
        }
    }


}

