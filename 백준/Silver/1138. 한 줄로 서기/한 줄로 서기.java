import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr =new int[N];
        for(int i=0; i<N; i++){
            int tmp = Integer.parseInt(st.nextToken());
            arr[i] = tmp;
        }
        int[] res = new int[N];
        for(int i=N-1, j=0; i>=0; i--, j++){
            int cnt = arr[i];
            if(cnt == j){
                res[j] = i+1;
            }else{
                for(int k=j; k>cnt; k--){
                    res[k] = res[k-1];
                }
                res[cnt] = i+1;
            }
        }
        for(int i=0; i<N; i++){
            System.out.print(res[i]+" ");
        }

    }

}
