import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] mindp = new int[]{0, 0, 0};
        int[] maxdp = new int[]{0, 0, 0};
        int[] dy = new int[]{-1, 0, 1};

        for (int i = 0; i < N; i += 2) {
            int[][] arr = new int[Math.min(N - i, 2)][3];
            for (int p = 0; p < arr.length; p++) {
                for (int j = 0; j < 3; j++) {
                    arr[p][j] = scanner.nextInt();
                }
            }
            for (int p = 0; p < arr.length; p++) {
                int[] tmpmindp = new int[3];
                int[] tmpmaxdp = new int[3];
                for (int j = 0; j < 3; j++) {
                    int minVal, maxVal;
                    if (j == 0) {
                        minVal = Math.min(mindp[0], mindp[1]);
                        maxVal = Math.max(maxdp[0], maxdp[1]);
                    } else if (j == 1) {
                        minVal = Math.min(mindp[0], Math.min(mindp[1], mindp[2]));
                        maxVal = Math.max(maxdp[0], Math.max(maxdp[1], maxdp[2]));
                    } else {
                        minVal = Math.min(mindp[1], mindp[2]);
                        maxVal = Math.max(maxdp[1], maxdp[2]);
                    }
                    if (i != 0 || p != 0) {
                        tmpmindp[j] = minVal + arr[p][j];
                        tmpmaxdp[j] = maxVal + arr[p][j];
                    } else {
                        tmpmindp[j] = arr[p][j];
                        tmpmaxdp[j] = arr[p][j];
                    }
                }
                mindp = tmpmindp;
                maxdp = tmpmaxdp;
            }
        }
        int maxVal = Math.max(maxdp[0], Math.max(maxdp[1], maxdp[2]));
        int minVal = Math.min(mindp[0], Math.min(mindp[1], mindp[2]));
        System.out.println(maxVal + " " + minVal);
        scanner.close();
    }
}
