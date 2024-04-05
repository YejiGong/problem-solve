import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    static int[][] visit;
    static char[][] maps;
    static int R, C;
    static int[] v = new int[2]; // 비버 위치
    static int[] g = new int[2]; // 고슴도치 위치
    static Queue<int[]> waterq = new LinkedList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        R = scanner.nextInt();
        C = scanner.nextInt();

        visit = new int[R][C];
        maps = new char[R][C];

        scanner.nextLine();
        for (int i = 0; i < R; i++) {
            String line = scanner.nextLine();
            for (int j = 0; j < C; j++) {
                maps[i][j] = line.charAt(j);
                visit[i][j] = -1;
                if (maps[i][j] == 'D') {
                    v[0] = i;
                    v[1] = j;
                } else if (maps[i][j] == 'S') {
                    g[0] = i;
                    g[1] = j;
                } else if (maps[i][j] == '*') {
                    waterq.offer(new int[]{i, j, 0});
                    visit[i][j] = 0;
                }
            }
        }

        while (!waterq.isEmpty()) {
            int[] water = waterq.poll();
            int t = water[2];
            for (int k = 0; k < 4; k++) {
                int nx = water[0] + dx[k];
                int ny = water[1] + dy[k];
                if (nx >= 0 && nx < R && ny >= 0 && ny < C && visit[nx][ny] == -1 && maps[nx][ny] != 'X' && maps[nx][ny] != 'D') {
                    visit[nx][ny] = t + 1;
                    waterq.offer(new int[]{nx, ny, t + 1});
                }
            }
        }

        int res = bfs();
        if (res != -1)
            System.out.println(res);
        else
            System.out.println("KAKTUS");
    }

    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};

    static int bfs() {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{g[0], g[1], 0});

        while (!queue.isEmpty()) {
            int[] pos = queue.poll();
            int x = pos[0];
            int y = pos[1];
            int t = pos[2];

            if (x == v[0] && y == v[1])
                return t;

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && nx < R && ny >= 0 && ny < C && (visit[nx][ny] == -1 || visit[nx][ny] > t + 1) && maps[nx][ny] != 'X') {
                    visit[nx][ny] = -2;
                    queue.offer(new int[]{nx, ny, t + 1});
                }
            }
        }
        return -1;
    }
}
