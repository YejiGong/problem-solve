import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        ArrayList<Integer> arr = new ArrayList<Integer>();
        Deque<Integer> dq = new LinkedList<Integer>();
        for(int i=0; i<N; i++){
            arr.add(i+1);
        }
        int cnt = K-1;
        while(arr.size()>1){
            int tmp = arr.remove(cnt);
            dq.add(tmp);
            cnt = (cnt+K-1)%arr.size();
        }
        dq.add(arr.get(0));
        System.out.print("<"+dq.poll());
        while(dq.size()>0){
            System.out.print(", "+dq.poll());
        }
        System.out.println(">");
    }

}
