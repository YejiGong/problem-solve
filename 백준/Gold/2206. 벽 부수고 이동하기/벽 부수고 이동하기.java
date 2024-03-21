import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();
        scanner.nextLine();

        int[][] graph = new int[N][M];
        int[][][] visited = new int[N][M][2];
        for (int i = 0; i < N; i++) {
            String row = scanner.nextLine();
            for (int j = 0; j < M; j++) {
                graph[i][j] = row.charAt(j) - '0';
            }
        }
        visited[0][0][0] = 1;
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{0, 0, 0});

        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];
            int z = current[2];

            if (x == N - 1 && y == M - 1) {
                System.out.println(visited[x][y][z]);
                return;
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
                    continue;
                }

                if (graph[nx][ny] == 1 && z == 0) {
                    visited[nx][ny][1] = visited[x][y][0] + 1;
                    queue.offer(new int[]{nx, ny, 1});
                } else if (graph[nx][ny] == 0 && visited[nx][ny][z] == 0) {
                    visited[nx][ny][z] = visited[x][y][z] + 1;
                    queue.offer(new int[]{nx, ny, z});
                }
            }
        }
        System.out.println(-1);
    }
}
