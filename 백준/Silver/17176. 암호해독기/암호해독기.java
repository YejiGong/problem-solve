import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N]; //암호문
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] res_cnt = new int[53];
        for(int i=0; i<N; i++){
            int tmp = Integer.parseInt(st.nextToken());
            arr[i] = tmp;
            res_cnt[tmp]++;
        }

        String strs = br.readLine(); //평문
        int[] cnt = new int[53];
        int white_space = 0;
        for(int i=0; i<strs.length(); i++){
            char c = strs.charAt(i);
            if(c ==' '){
                cnt[0]++;
            }else {
                if(c-'A'>=32) { //소문자
                    cnt[c - 'A' - 5]++;
                }else{
                    cnt[c-'A'+1]++;
                }
            }
        }
        for(int i=0; i<=52; i++){
            if(res_cnt[i]!=cnt[i]){
                System.out.println("n");
                return;
            }
        }
        System.out.println("y");



    }

}
