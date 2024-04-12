import java.util.Scanner;

public class Main {
    static int[][] graph;
    static int N;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        N = Integer.parseInt(scanner.nextLine());
        graph = new int[N][N];

        for (int i = 0; i < N; i++) {
            String[] input = scanner.nextLine().split(" ");
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(input[j]);
            }
        }

        while (true) {
            if (check() == 0) {
                break;
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(graph[i][j] + " ");
            }
            System.out.println();
        }
    }

    static int check() {
        int tmp = 0;
        for (int k = 0; k < N; k++) {
            for (int a = 0; a < N; a++) {
                if (graph[k][a] == 1) {
                    for (int b = 0; b < N; b++) {
                        if (graph[a][b] == 1 && graph[k][b] == 0) {
                            tmp++;
                            graph[k][b] = 1;
                        }
                    }
                }
            }
        }
        return tmp;
    }
}
