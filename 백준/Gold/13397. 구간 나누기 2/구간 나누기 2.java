import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int M;
    static int[] arr;
    public static int cal(int mid){
        int cnt=1;
        int minValue = arr[0];
        int maxValue = arr[0];
        for(int i=0; i<N; i++){
            minValue = Math.min(minValue, arr[i]);
            maxValue = Math.max(maxValue, arr[i]);
            if(maxValue-minValue>mid){
                cnt+=1;
                minValue = arr[i];
                maxValue = arr[i];
            }

        }
        return cnt;
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N= Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        arr = new int[N];
        for(int i=0; i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        //M-1개 이하의 구분칸이 필요하다.
        int left = 0; int right = Arrays.stream(arr).max().getAsInt(); int ans=right;
        while(left<=right){
            int mid = (left+right)/2;
            if(cal(mid)<=M){
                if(ans>mid){
                    ans= mid;
                }
                right = mid-1;
            }else{
                left=mid+1;
            }
        }
        System.out.println(ans);

    }


}
