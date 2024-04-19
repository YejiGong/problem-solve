import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        PriorityQueue<Integer> queue = new PriorityQueue<>();

        int n = scanner.nextInt();
        while (n > 0) {
            n--;
            int tmp = scanner.nextInt();
            queue.offer(tmp);
        }

        int answer = 0;
        while (queue.size() > 1) {
            int a = queue.poll();
            int b = queue.poll();
            answer += (a + b);
            queue.offer(a + b);
        }

        System.out.println(answer);
    }
}
