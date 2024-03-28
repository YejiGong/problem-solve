import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();

        int[] lecture = new int[N];
        for (int i = 0; i < N; i++) {
            lecture[i] = scanner.nextInt();
        }

        int left = 0;
        int right = 0;
        for (int t : lecture) {
            left = Math.max(left, t);
            right += t;
        }

        int ans = 0;
        while (left <= right) {
            int mid = (left + right) / 2;
            int cnt = 1;
            int tmp = 0;
            for (int t : lecture) {
                if (t + tmp > mid) {
                    cnt++;
                    tmp = 0;
                }
                tmp += t;
            }
            if (cnt <= M) {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        System.out.println(ans);
    }
}
