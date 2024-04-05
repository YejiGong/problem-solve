import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    static int[][] graph;
    static int[][] visited;
    static int N, M;
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt();
        M = scanner.nextInt();

        graph = new int[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                graph[i][j] = scanner.nextInt();
            }
        }

        int idx = 0;
        while (true) {
            int check = 0;
            visited = new int[N][M];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (graph[i][j] != 0 && visited[i][j] == 0) {
                        visited[i][j] = 1;
                        bfs(i, j);
                        check++;
                    }
                }
            }
            if (check == 1) {
                idx++;
            } else if (check >= 2) {
                System.out.println(idx);
                break;
            } else if (check == 0) {
                System.out.println(0);
                break;
            }
        }
    }

    static void bfs(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{x, y});
        while (!queue.isEmpty()) {
            int[] pos = queue.poll();
            int result = 0;
            int px = pos[0];
            int py = pos[1];
            for (int i = 0; i < 4; i++) {
                int nx = px + dx[i];
                int ny = py + dy[i];
                if (nx >= 0 && nx < N && ny >= 0 && ny < M && visited[nx][ny] == 0) {
                    if (graph[nx][ny] == 0) {
                        result++;
                    } else {
                        visited[nx][ny] = 1;
                        queue.offer(new int[]{nx, ny});
                    }
                }
            }
            graph[px][py] = Math.max(graph[px][py] - result, 0);
        }
    }
}
