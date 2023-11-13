import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int M;
    static int[] arr;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        N = Integer.parseInt(br.readLine());
        arr = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        M = Integer.parseInt(br.readLine());
        if(Arrays.stream(arr).sum()<=M){
            System.out.println(Arrays.stream(arr).max().getAsInt());
        }else{
            System.out.println(binarySearch());
        }
    }

    public static int binarySearch(){
        int left = 0;
        int right = Arrays.stream(arr).max().getAsInt();
        int ans = 0;
        while(left<=right){
            int mid = (left+right)/2;
            int sumResult = Arrays.stream(arr).map(val->Math.min(val, mid)).sum();
            if(sumResult==M){
                ans = mid;
                break;
            }
            if(sumResult<M){
                ans = mid;
                left=mid+1;
            }
            else{
                right=mid-1;
            }
        }
        return ans;

    }



}
