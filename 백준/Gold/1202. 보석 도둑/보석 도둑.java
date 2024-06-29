import java.io.*;
import java.util.*;
import java.lang.Math;

public class Main {
    public static class Jewel implements Comparable<Jewel>{
        int weight;
        int value;
        public Jewel(int weight, int value){
            this.weight = weight;
            this.value = value;
        }
        @Override
        public int compareTo(Jewel o){
            if(this.weight == o.weight){
                return o.value - this.value;
            }
            return this.weight - o.weight;
        }
        @Override
        public String toString(){
            return
                    "weight=" + weight +
                            ", value=" + value + ";";
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        List<Jewel> jewels = new ArrayList<>();
        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            int M = Integer.parseInt(st.nextToken());
            int V = Integer.parseInt(st.nextToken());
            jewels.add(new Jewel(M,V));
        }
        List<Integer> bags = new ArrayList<>();
        for(int i=0; i<K; i++){
            int C = Integer.parseInt(br.readLine());
            bags.add(C);
        }
        Collections.sort(jewels);
        Collections.sort(bags); //내림차순
        long result = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        int jewelIdx =0;
        for(int i=0; i<K; i++){
            while(jewelIdx<N && jewels.get(jewelIdx).weight<=bags.get(i)){
                pq.add(-jewels.get(jewelIdx).value);
                jewelIdx++;
            }
            if(!pq.isEmpty()){
                result += pq.poll();
            }
            if(jewels.isEmpty() && pq.isEmpty()){
                break;
            }
        }
        System.out.println(-result);
    }
}
