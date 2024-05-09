import java.io.*;
import java.util.*;

public class Main {
    public static class Node implements Comparable<Node>{
        int index;
        int cost;
        public Node(int index, int cost){
            this.index = index;
            this.cost = cost;
        }
        @Override
        public int compareTo(Node o1){
            return this.cost - o1.cost;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        LinkedList<Node>[] graph = new LinkedList[N+1];
        for(int i=0; i<N+1; i++){
            graph[i] = new LinkedList<>();
        }
        StringTokenizer st;
        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph[a].add(new Node(b,c));
        }
        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int finish = Integer.parseInt(st.nextToken());
        int[] dist = new int[N+1];
        boolean[] visit = new boolean[N+1];
        int[] prev = new int[N+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        Arrays.fill(visit, false);
        dist[start] = 0;
        PriorityQueue<Node> q = new PriorityQueue<Node>();
        q.add(new Node(start,0));
        while(!q.isEmpty()){
            Node tmp = q.poll();
            if(visit[tmp.index]) continue;
            visit[tmp.index] = true;
            for(Node node: graph[tmp.index]){
                if(!visit[node.index] && dist[node.index]>dist[tmp.index]+node.cost){
                    dist[node.index] = dist[tmp.index]+node.cost;
                    prev[node.index] = tmp.index;
                    q.add(new Node(node.index, dist[node.index]));
                }
            }
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(dist[finish]+""+"\n");
        Stack<Integer> stack = new Stack<>();
        int tmp = finish;
        while(tmp!=0){
            stack.push(tmp);
            tmp = prev[tmp];
        }
        bw.write(stack.size()+"\n");
        while(!stack.isEmpty()){
            bw.write(stack.pop()+" ");
        }
        bw.close();

    }

}

