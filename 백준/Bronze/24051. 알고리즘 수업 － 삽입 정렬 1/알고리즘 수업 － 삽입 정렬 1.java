import java.util.List;
import java.util.Scanner;
import java.util.LinkedList;
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
        int result = insertion_sort(K);
        System.out.println(result);
    }

    public static int insertion_sort(int num){
        int cnt = 0;
        for(int i=1; i<N; i++){
            int loc = i -1;
            int newItem= arr[i];

            while(0<=loc && newItem<arr[loc]){
                arr[loc+1]=arr[loc];
                cnt++;
                if(cnt==num){
                    return arr[loc+1];
                }
                loc--;
            }
            if(loc+1!=i){
                arr[loc+1]=newItem;
                cnt++;
                if(cnt==num){
                    return arr[loc+1];
                }
            }
        }

        return -1;
    }
}
