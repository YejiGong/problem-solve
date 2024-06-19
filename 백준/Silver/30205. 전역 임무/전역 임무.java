import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        long K = Long.parseLong(st.nextToken());
        boolean flag = true;
        for(int i=0; i<N; i++){
            int item = 0;
            st = new StringTokenizer(br.readLine());
            PriorityQueue<Integer> pq = new PriorityQueue<>();
            for(int j=0; j<M; j++){
                int tmp = Integer.parseInt(st.nextToken());
                if(tmp==-1){
                    item ++;
                }else{
                    pq.offer(tmp);
                }
            }

            while(flag && !pq.isEmpty()){
                while(K<pq.peek() && item>0){
                    item --;
                    K *= 2;
                }

                if(K<pq.peek()){
                    flag = false;
                    System.out.println("0");
                    break;
                }

                K += pq.peek();
                pq.poll();
            }

            while(item-- > 0) K*=2;
        }

        if(flag){
            System.out.println("1");
        }

    }


}

