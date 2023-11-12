import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int M;
    static Criteria[] limitValues;
    public static class Criteria{
        String name;
        int value;
        public Criteria(String name, int value){
            this.name = name;
            this.value = value;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        limitValues = new Criteria[N];
        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            int value = Integer.parseInt(st.nextToken());
            limitValues[i] = new Criteria(name, value);
        }

        for(int i=0; i<M; i++){
            int val = Integer.parseInt(br.readLine());
            bw.write(binarySearch(val));
            bw.newLine();
        }
        bw.flush();
    }

    public static String binarySearch(int value){
        int left = 0;
        int right = N-1;
        int ans = 0;
        while(left<=right){
            int mid = (left+right)/2;
            if(value<=limitValues[mid].value){
                ans = mid;
                right = mid-1;
            }
            else{
                left = mid+1;
            }
        }
        return limitValues[ans].name;

    }



}
