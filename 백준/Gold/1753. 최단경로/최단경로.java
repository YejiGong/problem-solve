import java.util.*;

public class Main {
    static final int INF = Integer.MAX_VALUE;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int v = scanner.nextInt(); // 정점의 수
        int e = scanner.nextInt(); // 간선의 수
        int k = scanner.nextInt(); // 시작 정점

        List<List<Node>> graph = new ArrayList<>();
        for (int i = 0; i <= v; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < e; i++) {
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            int w = scanner.nextInt();
            graph.get(x).add(new Node(y, w)); // u->v 간선 가중치 w.
        }

        int[] distance = new int[v + 1];
        Arrays.fill(distance, INF); // 초기값

        dijkstra(graph, distance, k);

        for (int i = 1; i <= v; i++) {
            if (distance[i] == INF) {
                System.out.println("INF");
            } else {
                System.out.println(distance[i]);
            }
        }
    }

    static class Node {
        int y;
        int weight;

        Node(int y, int weight) {
            this.y = y;
            this.weight = weight;
        }
    }

    static void dijkstra(List<List<Node>> graph, int[] distance, int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a.weight));
        pq.offer(new Node(start, 0));
        distance[start] = 0;

        while (!pq.isEmpty()) {
            Node node = pq.poll();
            int now = node.y;
            int dist = node.weight;

            if (distance[now] < dist) continue;

            for (Node next : graph.get(now)) {
                int cost = dist + next.weight;

                if (cost < distance[next.y]) {
                    distance[next.y] = cost;
                    pq.offer(new Node(next.y, cost));
                }
            }
        }
    }
}
