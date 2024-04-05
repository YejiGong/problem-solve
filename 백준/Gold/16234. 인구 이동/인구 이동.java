import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    static int[][] people;
    static int[][] visited;
    static int N, L, R;
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt();
        L = scanner.nextInt();
        R = scanner.nextInt();
        people = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                people[i][j] = scanner.nextInt();
            }
        }

        int result = 0;
        while (true) {
            boolean flag = false;
            visited = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (visited[i][j] == 0) {
                        Queue<int[]> boundaryTmp = new LinkedList<>();
                        int sumTmp = bfs(i, j, boundaryTmp);
                        if (boundaryTmp.size() > 1) {
                            flag = true;
                            int tmpResult = sumTmp / boundaryTmp.size();
                            for (int[] k : boundaryTmp) {
                                people[k[0]][k[1]] = tmpResult;
                            }
                        }
                    }
                }
            }
            if (flag) {
                result++;
            } else {
                break;
            }
        }

        System.out.println(result);
    }

    static int bfs(int x, int y, Queue<int[]> boundaryTmp) {
        int sumTmp = 0;
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{x, y});
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int cx = current[0];
            int cy = current[1];
            visited[cx][cy] = 1;
            boundaryTmp.offer(new int[]{cx, cy});
            sumTmp += people[cx][cy];
            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                if (nx >= 0 && nx < N && ny >= 0 && ny < N && visited[nx][ny] == 0
                        && L <= Math.abs(people[nx][ny] - people[cx][cy]) && Math.abs(people[nx][ny] - people[cx][cy]) <= R) {
                    visited[nx][ny] = 1;
                    queue.offer(new int[]{nx, ny});
                }
            }
        }
        return sumTmp;
    }
}
