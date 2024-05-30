import java.io.*;
import java.util.*;

public class Main {
    public static int N;
    public static int K;
    public static List<int[]> result;
    public static int[] arr;
    public static int[] tmp;
    public static int res = 0;
    public static boolean[] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        result = new ArrayList<>();
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        arr = new int[N];
        for(int i=0; i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        tmp = new int[N];
        visited = new boolean[N];
        perm(0);
        System.out.println(res);

    }

    public static void perm(int depth){
        if(depth==N){
            result.add(tmp);
            if(check(arr, tmp)){
                res+=1;
            }
            return;
        }
        for(int i=0; i<N; i++){
            if(visited[i]) continue;
            tmp[depth] = i;
            visited[i] = true;
            perm(depth+1);
            visited[i] = false;
        }
    }

    public static Boolean check(int[] arr, int[] perm){
        int sum = 500;
        for(int i=0; i<N; i++){
            sum -= K;
            sum += arr[perm[i]];
            if(sum<500){
                return false;
            }
        }
        return true;
    }

}

