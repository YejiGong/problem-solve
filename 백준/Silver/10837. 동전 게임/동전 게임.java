import java.io.*;
import java.util.*;

public class Main {
    public static int K;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        K = Integer.parseInt(br.readLine());
        int C = Integer.parseInt(br.readLine());
        StringTokenizer st;
        for(int i=0; i<C; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if(isPossible(a,b) == true){
                System.out.println("1");
            }else{
                System.out.println("0");
            }
        }

    }

    public static boolean isPossible(int a, int b){
        if(a==b){
            return true;
        }
        int diff = Math.abs(a-b);
        if(a>b){
            int leftNum = K - a;
            if(diff>leftNum+2){
                return false;
            }
        }
        if(b>a){
            int leftNum = K - b;
            if(diff>leftNum+1){
                return false;
            }
        }
        return true;
    }

}
