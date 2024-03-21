import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        scanner.nextLine();

        int[][] graph = new int[n][m];
        for (int i = 0; i < n; i++) {
            String line = scanner.nextLine();
            for (int j = 0; j < m; j++) {
                graph[i][j] = line.charAt(j) - '0';
            }
        }

        int[][] dp = new int[n][m];
        int[] dx = {0, -1, -1};
        int[] dy = {-1, -1, 0};

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 1) {
                    boolean flag = true;
                    int val = Integer.MAX_VALUE;
                    for (int k = 0; k < 3; k++) {
                        int nx = i + dx[k];
                        int ny = j + dy[k];
                        if (nx >= 0 && nx < n && ny >= 0 && ny < m && graph[nx][ny] == 1) {
                            val = Math.min(val, dp[nx][ny]);
                        } else {
                            flag = false;
                            break;
                        }
                    }
                    if (flag) {
                        if (val != Integer.MAX_VALUE) {
                            dp[i][j] = Math.max(2, val + 1);
                        } else {
                            dp[i][j] = 2;
                        }
                    } else {
                        dp[i][j] = 1;
                    }
                }
            }
        }

        int maxVal = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                maxVal = Math.max(maxVal, dp[i][j]);
            }
        }
        System.out.println(maxVal * maxVal);
        scanner.close();
    }
}
