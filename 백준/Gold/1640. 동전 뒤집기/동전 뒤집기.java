import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] graph = new int[N][M];
        int[] rowdp = new int[N];
        int[] coldp = new int[M];
        for(int i=0; i<N; i++){
            String tmp = br.readLine();
            for(int j=0; j<M; j++){
                graph[i][j] = Integer.parseInt(tmp.substring(j, j+1));
                if(graph[i][j]==1){
                    rowdp[i]++;
                    coldp[j]++;
                }
            }
        }
        int r = 0;
        int c = 0;
        for(int i=0; i<N; i++){
            r += rowdp[i]%2;
        }
        for(int i=0; i<M; i++){
            c += coldp[i]%2;
        }
        if(r%2==0 && c%2==0){
            System.out.println(Math.min(r+c, N-r+M-c));
        }
        else if(r%2==1 && c%2==1){
            System.out.println(Math.min(r+M-c, c+N-r));
        }else{
            System.out.println("-1");
        }

    }

}

