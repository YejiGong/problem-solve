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
        arr = new int[N];
        st = new StringTokenizer(br.readLine());
        int maxNum = 0;
        for(int i=0; i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int visit[] = new int[maxNum+1];
        Arrays.fill(visit,0);
        int start=0; int end=0; int ans=0; int cnt=0; int tmp_ans=0;
        while(start<=end){
            if(cnt>K){
                ans = Math.max(ans, tmp_ans);
                start++;
                end--;
                cnt--;
                tmp_ans--;
            }
            if(end>=N){
                ans = Math.max(ans,tmp_ans);
                break;
            }
            if(arr[start]%2!=0){
                start++;
                end=Math.max(end,start);
                tmp_ans= Math.max(tmp_ans,0);
                cnt=Math.max(cnt-1,0);
            }
            else{
                //수열 길이 재기 시작
                if(arr[end]%2==0){
                    end++;
                    tmp_ans++;
                }else{
                    cnt++;
                    end++;
                }
            }
        }
        System.out.println(ans);
    }

}
