import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.LinkedList;
import java.util.stream.Collectors;

public class Main {
    static int[] arr;
    static int N;
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt();
        int K = scanner.nextInt();
        arr = new int[N];
        for(int i=0; i<N; i++){
            int num = scanner.nextInt();
            arr[i] = num;
        }
        int result = bubble_sort(K);
    }

    public static int bubble_sort(int num){
        int cnt = 0;
        for(int last = N-1; last>0; last--){
            for(int i=0; i<last; i++){
                if(arr[i]>arr[i+1]){
                    int tmp = arr[i];
                    arr[i] = arr[i+1];
                    arr[i+1] = tmp;
                    cnt++;
                    if(cnt==num){
                        System.out.println(Arrays.stream(arr).mapToObj(String::valueOf).collect(Collectors.joining(" ")));
                        return -1;
                    }
                }
            }
        }
        System.out.println("-1");
        return -1;
    }
}
