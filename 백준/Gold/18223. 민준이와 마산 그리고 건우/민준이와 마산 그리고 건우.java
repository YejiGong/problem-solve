import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
    static int V;
    static int E;
    static int P;
    static boolean visit[];
    static int dist[];
    static ArrayList<ArrayList<Node>> list;


    static class Node{
        int idx;
        int cost;
        Node(int idx, int cost){
            this.idx = idx;
            this.cost = cost;
        }
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        V = scanner.nextInt(); E = scanner.nextInt(); P = scanner.nextInt();
        visit = new boolean[V+1];
        dist = new int[V+1];
        Arrays.fill(visit,false);
        Arrays.fill(dist, Integer.MAX_VALUE);
        list = new ArrayList<ArrayList<Node>>();
        for(int i=0; i<V+1; i++){
            list.add(new ArrayList<>());
        }

        for(int i=0; i<E; i++){
            int a = scanner.nextInt(); int b = scanner.nextInt(); int c = scanner.nextInt();
            list.get(a).add(new Node(b,c));
            list.get(b).add(new Node(a,c));
        }
        //1-V를 구하되, 이 경로에 P가 포함되는지 확인
        int s=1; int e=V;
        dist[s] = 0;
        for(int i=0; i<V; i++){
            int cntV = Integer.MAX_VALUE;
            int cntIdx = 0;
            for(int j=1; j<V+1; j++){
                if(!visit[j] && dist[j]<cntV){
                    cntV = dist[j];
                    cntIdx = j;
                }
            }
            visit[cntIdx] = true;

            for(int j=0; j<list.get(cntIdx).size(); j++){
                int idx = list.get(cntIdx).get(j).idx;
                int cost = list.get(cntIdx).get(j).cost;
                if(!visit[idx] && dist[idx]>dist[cntIdx]+cost){
                    dist[idx] = dist[cntIdx]+cost;
                }
            }
        }
        int distV = dist[V];
        int distP = dist[P];

        Arrays.fill(visit,false);
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[P]=0;
        for(int i=0; i<V; i++){
            int cntV = Integer.MAX_VALUE;
            int cntIdx = P;
            for(int j=1; j<V+1; j++){
                if(!visit[j] && dist[j]<cntV){
                    cntV = dist[j];
                    cntIdx = j;
                }
            }
            visit[cntIdx] = true;

            for(int j=0; j<list.get(cntIdx).size(); j++){
                int idx = list.get(cntIdx).get(j).idx;
                int cost = list.get(cntIdx).get(j).cost;
                if(!visit[idx] && dist[idx]>dist[cntIdx]+cost){
                    dist[idx] = dist[cntIdx]+cost;
                }
            }
        }
        int distPV = dist[V];
        if(distP+distPV<=distV) {
            System.out.println("SAVE HIM");
        }else{
            System.out.println("GOOD BYE");
        }
    }

}
