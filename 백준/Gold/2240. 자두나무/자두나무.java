import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        int W = scanner.nextInt();

        int[] tree_one = new int[T + 1];
        int[] tree_two = new int[T + 1];

        for (int t = 1; t <= T; t++) {
            int tree = scanner.nextInt();
            if (tree == 1) {
                tree_one[t] = 1;
            } else {
                tree_two[t] = 1;
            }
        }

        int[][] dp = new int[W + 1][T + 1];
        int[] W1 = new int[T + 1];
        int[] W2 = new int[T + 1];

        for (int i = 0; i <= T; i++) {
            if (i == 0) {
                W1[i] = sum(tree_one);
                W2[i] = sum(tree_two);
            } else {
                W1[i] = sum(tree_one, 0, i) + sum(tree_two, i, T + 1);
                W2[i] = sum(tree_two, 0, i) + sum(tree_one, i, T + 1);
                dp[1][i] = Math.max(W1[i], dp[1][i - 1]);
            }
        }
        dp[1][0] = W1[0];

        for (int i = 2; i <= W; i++) {
            for (int j = 1; j <= T; j++) {
                if (i % 2 == 0) {
                    dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j] + W2[j] - W2[0]);
                } else {
                    dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j] + W1[j] - W1[0]);
                }
            }
        }

        int maxVal = dp[1][0];
        for (int i = 1; i <= W; i++) {
            maxVal = Math.max(maxVal, dp[i][T]);
        }
        System.out.println(maxVal);
        scanner.close();
    }

    private static int sum(int[] array) {
        int sum = 0;
        for (int num : array) {
            sum += num;
        }
        return sum;
    }

    private static int sum(int[] array, int start, int end) {
        int sum = 0;
        for (int i = start; i < end; i++) {
            sum += array[i];
        }
        return sum;
    }
}
