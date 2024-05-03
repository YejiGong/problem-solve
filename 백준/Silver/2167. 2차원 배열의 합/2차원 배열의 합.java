import java.io.*;
import java.util.*;

public class Main {
    static int[][] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.valueOf(st.nextToken());
        int M = Integer.valueOf(st.nextToken());
        arr = new int[N][M];
        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<M; j++){
                int tmp = Integer.valueOf(st.nextToken());
                arr[i][j] = tmp;
            }
        }
        int K = Integer.valueOf(br.readLine());
        for(int k=0; k<K; k++){
            st = new StringTokenizer(br.readLine());
            int i = Integer.valueOf(st.nextToken());
            int j = Integer.valueOf(st.nextToken());
            int x = Integer.valueOf(st.nextToken());
            int y = Integer.valueOf(st.nextToken());
            System.out.println(getResult(i-1, j-1, x-1, y-1));
        }
    }

    public static int getResult(int i, int j, int x, int y){
        int result = 0;
        for(int a=i; a<=x; a++){
            for(int b=j; b<=y; b++){
                result += arr[a][b];
            }
        }
        return result;
    }

}
