import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    static ArrayList<Integer> pre = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (scanner.hasNextLine()) {
            try {
                pre.add(Integer.parseInt(scanner.nextLine()));
            } catch (Exception e) {
                break;
            }
        }

        post(0, pre.size() - 1);
    }

    static void post(int start, int end) {
        if (start > end) {
            return;
        }
        int mid = end + 1;
        for (int i = start + 1; i <= end; i++) {
            if (pre.get(i) > pre.get(start)) {
                mid = i;
                break;
            }
        }
        post(start + 1, mid - 1); // 왼쪽 트리
        post(mid, end); // 오른쪽 트리
        System.out.println(pre.get(start)); // 루트 노드
    }
}
