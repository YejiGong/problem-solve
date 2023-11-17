import java.lang.reflect.Array;
import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int[][] arr;
    static ArrayList<edge>[] graph;
    static PriorityQueue<edge> pq = new PriorityQueue<>();
    static boolean[] visited;
    static long result;
    static int count;

    static class edge implements Comparable<edge>{
        int node;
        int weight;
        public edge(int node, int weight){
            this.node=node;
            this.weight = weight;
        }
        @Override
        public int compareTo(edge o){
            return weight - o.weight;
        }
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N+1][N+1];
        visited = new boolean[N+1];
        graph = new ArrayList[N+1];
        StringTokenizer st;
        for(int i=1; i<N+1; i++){
            st = new StringTokenizer(br.readLine());
            graph[i] = new ArrayList<>();
            for(int j=1; j<N+1; j++){
                int w = Integer.parseInt(st.nextToken());
                graph[i].add(new edge(j,w));
            }
        }
        prim();
        System.out.println(result);

    }
    static void prim(){
        pq.add(new edge(1,0));
        while(!pq.isEmpty()){
            edge cur = pq.poll();
            if(visited[cur.node]){
                continue;
            }
            visited[cur.node]=true;
            result+=cur.weight;
            for(edge next: graph[cur.node]){
                if(!visited[next.node]){
                    pq.add(next);
                }
            }
            if(++count==N){
                break;
            }
        }
    }
}
