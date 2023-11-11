import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int M;
    static int start;
    static int finish;
    static ArrayList<Num> check[];
    static boolean[] visit;
    public static class Num{
        int number;
        int weight;
        public Num(int number, int weight){
            this.number = number;
            this.weight = weight;
        }
    }

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        N= sc.nextInt();
        M = sc.nextInt();
        check = new ArrayList[N+1];
        for(int i=0; i<N+1; i++){
            check[i] = new ArrayList<Num>();
        }
        int minV = 0; int maxV = Integer.MAX_VALUE;
        for(int i=0; i<M; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            minV = Math.min(minV, c);
            maxV = Math.max(maxV, c);
            check[a].add(new Num(b,c));
            check[b].add(new Num(a,c));
        }
        start = sc.nextInt();
        finish = sc.nextInt();
        int result = 0;
        while(minV<=maxV){
            int mid = (minV+maxV)/2;
            visit = new boolean[N+1];
            if(bfs(mid)){
                result=mid;
                minV=mid+1;
            }else{
                maxV=mid-1;
            }
        }
        System.out.println(result);


    }

    public static boolean bfs(int mid){
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);

        while(!queue.isEmpty()){
            int cnt = queue.poll();
            visit[cnt]=true;
            if(cnt==finish) {
                return true;
            }
            for(int i=0; i<check[cnt].size(); i++){
                Num tmp = check[cnt].get(i);
                if(tmp.weight>=mid && visit[tmp.number]==false){
                    visit[tmp.number]=true;
                    queue.add(tmp.number);
                }
            }
        }
        return false;
    }


}
