import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] arr = new int[N+1];
        for(int i=1; i<N+1; i++){
            arr[i] = i;
        }
        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            arr[x]+=1;
            arr[y]-=1;
        }
        int[] visit = new int[N+1];
        for(int i=1; i<N; i++){
            if(visit[arr[i]]==1){
                System.out.println(-1);
                return;
            }else{
                visit[arr[i]]=1;
            }
        }
        for(int i=1; i<N+1; i++){
            System.out.print(arr[i]+" ");
        }





    }


}
