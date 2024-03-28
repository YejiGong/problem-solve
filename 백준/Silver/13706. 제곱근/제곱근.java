import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        BigInteger N = scanner.nextBigInteger();

        BigInteger start = BigInteger.ZERO;
        BigInteger end = N;
        
        while (start.compareTo(end) < 0) {
            BigInteger mid = start.add(end).divide(BigInteger.valueOf(2));
            BigInteger square = mid.multiply(mid);
            
            int comparison = square.compareTo(N);
            if (comparison == 0) {
                System.out.println(mid);
                return; // 정답을 찾으면 프로그램 종료
            } else if (comparison < 0) {
                start = mid.add(BigInteger.ONE); // 중간 값보다 작은 구간 버리기
            } else {
                end = mid; // 중간 값보다 큰 구간 버리기
            }
        }
    }
}
