import java.util.*;
import java.io.*;

public class Main {
    static int[] point;
    public static int lowerBinarySearch(int start, int finish){
        int left=0; int right=point.length-1; int mid=0;
        while(left<=right){
            mid=(left+right)/2;
            if(point[mid]==start){
                break;
            }
            else if(point[mid]>start){
                right = mid-1;
            }
            else{
                left = mid+1;
            }
        }
        if(point[mid]>=start){
            return mid;
        }
        else{
            return mid+1;
        }
    }
    public static int upperBinarySearch(int start, int finish){
        int left=0; int right=point.length-1; int mid=0;
        while(left<=right){
            mid=(left+right)/2;
            if(point[mid]==finish){
                break;
            }
            else if(point[mid]>finish){
                right = mid-1;
            }
            else{
                left = mid+1;
            }
        }
        if(point[mid]<=finish) {
            return mid;
        }else{
            return mid-1;
        }
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N= Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        point = new int[N];
        for(int i=0; i<N; i++){
            point[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(point); //정렬
        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int finish = Integer.parseInt(st.nextToken());
            int leftIdx = lowerBinarySearch(start, finish); int rightIdx = upperBinarySearch(start, finish);
            System.out.println(rightIdx - leftIdx + 1);
        }


    }


}
