import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        long[] max_arr = new long[10000001];

        long sum = 0;
        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<N; j++){
                int tmp = Integer.parseInt(st.nextToken());
                sum += tmp;
                max_arr[tmp]++;
            }
        }
        long[] dp = new long[10000001];
        dp[0] = 0;
        for(int i=1; i<10000001; i++){
            dp[i] = dp[i-1] + max_arr[i];
        }
        //dp: i 이하의 숫자 개수
        int t=1;
        long tmpSum = 0;
        if(Math.round((double)sum/2) == 0){
            System.out.println("0");
        }else {
            while (true) {
                tmpSum += (dp[10000000] - dp[t - 1]);
                //t = 1-> S(1,N)
                //t = 2 -> 2*S(2,N)+S(1,N)
                //t = 3 -> 3*S(3,N)+2*S(2,N)+S(1,N)
                if (tmpSum >= Math.round((double) sum / 2)) {
                    System.out.println(t);
                    break;
                }
                t += 1;
            }
        }

    }


}

