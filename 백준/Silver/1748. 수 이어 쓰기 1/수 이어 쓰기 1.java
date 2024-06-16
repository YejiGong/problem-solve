import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int result = 0;
        int length = String.valueOf(N).length(); //N의 자릿수 계산
        //N의 자릿수가 10보다 작으면 N까지의 모든 수가 한 수. N
        //N의 자릿수가 100보다 작으면 9+(N-9)*2 = 9*10^0 + (N-(10^1-1))*2
        //N의 자릿수가 1000보다 작으면 9+90*2+(N-99)*3 = 9*10^0 + 9*10^1*2+(N-(10^2-1))*3
        //N의 자릿수가 10000보다 작으면 9+90*2+900*3+(N-999)*4
        if(length==1){
            result = N;
        }else {
            for (int i = 0; i < length; i++) {
                if (i == length - 1) {
                    result += (N - ((int) Math.pow(10, i) - 1)) * (i + 1);
                } else {
                    result += 9 * (int) Math.pow(10, i) * (i + 1);
                }
            }
        }
        System.out.println(result);

    }


}

