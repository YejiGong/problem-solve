import java.io.*;
import java.util.*;

public class Main {
    static class Jewel {
        int weight;
        int value;
        
        public Jewel(int weight, int value) {
            this.weight = weight;
            this.value = value;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        List<Jewel> jewels = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int M = Integer.parseInt(st.nextToken());
            int V = Integer.parseInt(st.nextToken());
            jewels.add(new Jewel(M, V));
        }

        List<Integer> bags = new ArrayList<>();
        for (int i = 0; i < K; i++) {
            int C = Integer.parseInt(br.readLine());
            bags.add(C);
        }

        // 정렬: 보석은 무게 오름차순, 가방은 용량 오름차순
        Collections.sort(jewels, Comparator.comparingInt(j -> j.weight));
        Collections.sort(bags);

        long result = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        int jewelIdx = 0;
        for (int bagCapacity : bags) {
            // 현재 가방 용량보다 작은 보석들을 우선순위 큐에 추가
            while (jewelIdx < N && jewels.get(jewelIdx).weight <= bagCapacity) {
                pq.offer(jewels.get(jewelIdx).value);
                jewelIdx++;
            }

            // 우선순위 큐에서 가장 가치가 큰 보석 하나를 선택하여 결과에 추가
            if (!pq.isEmpty()) {
                result += pq.poll();
            }
        }

        System.out.println(result);
    }
}
