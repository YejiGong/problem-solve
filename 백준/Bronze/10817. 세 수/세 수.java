import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int A = scanner.nextInt();
        int B = scanner.nextInt();
        int C = scanner.nextInt();
        List<Integer> arr = new LinkedList<>(List.of(A,B,C));
        Collections.sort(arr);
        System.out.println(arr.get(1));
    }
}