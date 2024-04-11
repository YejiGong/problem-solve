import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        String str = scanner.next();
        String ans = "NO";
        for(int idx = 1; idx<=N; ++idx){
            String substr1 = str.substring(0,idx);
            String substr2 = str.substring(N-idx);
            int cnt = 0;
            for(int j =0; j<substr1.length(); j++){
                if(substr1.charAt(j) != substr2.charAt(j)){
                    cnt++;
                }
            }
            if(cnt==1){
                ans="YES";
                break;
            }

        }
        System.out.println(ans);
    }

}
