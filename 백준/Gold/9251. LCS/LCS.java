import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String fir = scanner.nextLine().trim().toUpperCase();
        String sec = scanner.nextLine().trim().toUpperCase();
        
        int[][] dp = new int[fir.length() + 1][sec.length() + 1];

        for (int i = 1; i <= fir.length(); i++) {
            for (int j = 1; j <= sec.length(); j++) {
                if (fir.charAt(i - 1) == sec.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        System.out.println(dp[fir.length()][sec.length()]);
        scanner.close();
    }
}
