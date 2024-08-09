import java.util.ArrayList;
import java.util.BitSet;
import java.util.List;
import java.util.Scanner;

public class Main {

    // Greatest Common Divisor (GCD) function
    public static long gcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    // Least Common Multiple (LCM) function
    public static long lcm(long a, long b) {
        return a / gcd(a, b) * b;
    }

    // Check function to evaluate the condition
    public static long check(long mid, List<Long> primes, long n) {
        long ret = mid;
        int size = primes.size();

        for (int i = 1; i < (1 << size); i++) {
            boolean flag = true;
            long t = 1;
            int cnt = 0;
            for (int j = 0; j < size; j++) {
                if ((i & (1 << j)) == 0) continue;
                if (lcm(t, primes.get(j)) > mid){
                    flag = false;
                    break;
                }
                t = lcm(t, primes.get(j));
                cnt++;
            }
            if (flag) {
                long term = mid / t;
                ret += term * (cnt % 2 == 1 ? -1 : 1);
            }
        }
        return ret;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        long P = sc.nextLong();

        long oneBillion = 1_000_000_000;

        if (P == 2) {
            if (n * P > oneBillion) {
                System.out.println(0);
            } else {
                System.out.println(n * P);
            }
        } else if (P < 50) {
            List<Long> primes = new ArrayList<>();
            long[] allPrimes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47};
            for (long prime : allPrimes) {
                primes.add(prime);
            }

            // Filter primes list
            while (!primes.isEmpty() && primes.get(primes.size() - 1) >= P) {
                primes.remove(primes.size() - 1);
            }

            long lo = 0, hi = oneBillion;
            while (lo + 1 < hi) {
                long mid = (lo + hi) / 2;
                if (check(mid, primes, n) < n) {
                    lo = mid;
                } else {
                    hi = mid;
                }
            }

            if (hi * P > oneBillion) {
                System.out.println(0);
            } else {
                System.out.println(hi * P);
            }
        } else {
            BitSet bitset = new BitSet(20_000_001);
            for (int i = 2; i < P && i <= 20_000_000; i++) {
                if (bitset.get(i)) continue;
                for (int j = i; j <= 20_000_000; j += i) {
                    bitset.set(j);
                }
            }

            int cnt = 0;
            int pos = 0;
            for (int i = 1; i <= 20_000_000 && cnt < n; i++) {
                if (!bitset.get(i)) {
                    cnt++;
                    pos = i;
                }
            }

            if (cnt < n || pos * P > oneBillion) {
                System.out.println(0);
            } else {
                System.out.println(pos * P);
            }
        }
        sc.close();
    }
}
