import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int K;
    static int[] arr;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        arr = new int[N+1];
        st = new StringTokenizer(br.readLine());
        int maxNum = 0;
        for(int i=1; i<N+1; i++){
            arr[i] = Integer.parseInt(st.nextToken());
            maxNum = Math.max(maxNum,arr[i]);
        }
        int visit[] = new int[maxNum+1];
        Arrays.fill(visit,0);
        int start=1; int end=1; int ans=0;
        while(start<=end){
            if(end==N+1){
                ans=Math.max(ans,end-start);
                break;
            }
            visit[arr[end]]+=1;
            if(visit[arr[end]]<=K){
                end++;
            }else{
                ans=Math.max(ans,end-start);
                visit[arr[start]]-=1;
                visit[arr[end]]-=1;
                start++;
            }
        }
        System.out.println(ans);
    }

}
