import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int K = scanner.nextInt();
        int[] visit = new int[100001];
        int[] dict = new int[100001];

        Queue<Integer> queue = new LinkedList<>();
        queue.offer(N);
        visit[N] = 1;
        int res = 0;

        while (!queue.isEmpty()) {
            int x = queue.poll();
            int t = visit[x] - 1; // 시간을 visit 배열에 기록함

            if (x == K) {
                res = t;
                break;
            }

            if (x - 1 >= 0 && visit[x - 1] == 0) {
                visit[x - 1] = t + 2;
                dict[x - 1] = x;
                queue.offer(x - 1);
            }

            if (x + 1 <= 100000 && visit[x + 1] == 0) {
                visit[x + 1] = t + 2;
                dict[x + 1] = x;
                queue.offer(x + 1);
            }

            if (2 * x <= 100000 && visit[2 * x] == 0) {
                visit[2 * x] = t + 2;
                dict[2 * x] = x;
                queue.offer(2 * x);
            }
        }

        System.out.println(res);

        int[] arr = new int[res + 1];
        int idx = res;
        int t = K;
        while (t != N) {
            arr[idx--] = t;
            t = dict[t];
        }
        arr[idx] = N;

        for (int i = 0; i < res + 1; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
