import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        List<Long> menus = new LinkedList<>();
        for(int i=0; i<N; i++){
            long tmp = Long.parseLong(st.nextToken());
            menus.add(tmp);
        }
        menus.sort(Comparator.naturalOrder());
        long answer = 0L;
        long[] nums = new long[N+1];
        nums[0] = 1;
        for (int i = 1; i < N + 1; i++) {
            nums[i] = (nums[i - 1] * 2);
            nums[i] %= 1000000007;
        }
        for(int i=0; i<N; i++){
            answer += (nums[i] - nums[N-i-1]) * menus.get(i);
            answer %= 1000000007;
        }
        System.out.println(answer);


    }


}

