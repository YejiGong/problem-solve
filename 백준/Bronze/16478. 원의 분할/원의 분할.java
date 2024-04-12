import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();
        long m = scanner.nextLong();
        long k = scanner.nextLong();
        double result = (n * k * 1.0) / m / 1.0;
        System.out.printf("%.7f", result);
        scanner.close();
    }
}
