import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            try {
                int x = Integer.parseInt(scanner.nextLine()) * (int)Math.pow(10, 7); // 구멍의 너비
                int n = Integer.parseInt(scanner.nextLine());
                int[] nums = new int[n];
                for (int i = 0; i < n; i++) {
                    nums[i] = Integer.parseInt(scanner.nextLine()); // 레고 조각의 길이 -> cm로 변환해서 저장
                }
                Arrays.sort(nums);
                // l1+l1 = x여야한다. 만약 여러개라면 l2-l1의 값이 가장 큰 것으로.
                int start = 0, end = n - 1;
                List<int[]> queue = new ArrayList<>();
                while (start < n && end < n && start < end) {
                    if (nums[start] + nums[end] == x) {
                        queue.add(new int[]{start, end});
                        break;
                    } else {
                        if (nums[start] + nums[end] > x) {
                            end -= 1;
                        } else if (nums[start] + nums[end] < x) {
                            start += 1;
                        }
                    }
                }
                if (!queue.isEmpty()) {
                    System.out.println("yes " + nums[queue.get(0)[0]] + " " + nums[queue.get(0)[1]]);
                } else {
                    System.out.println("danger");
                }
            } catch (Exception e) {
                break;
            }
        }
    }
}
