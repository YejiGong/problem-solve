import java.util.List;
import java.util.Scanner;
import java.util.LinkedList;
public class Main {
    static int[] parent;
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int G = scanner.nextInt();
        int P = scanner.nextInt();
        List<Integer> gate = new LinkedList<Integer>();
        parent = new int[G+1];
        for(int i=0; i<G+1; i++){
            parent[i] = i;
        }
        int ans = 0;
        for (int i = 0; i < P; i++) {
            int c = scanner.nextInt();
            int emptyGate = find(c);
            if(emptyGate == 0){
                break;
            }

            ans++;
            union(emptyGate, emptyGate-1);
        }
        System.out.println(ans);
    }
    public static int find(int x){
        if(x==parent[x]){
            return x;
        }
        return parent[x] = find(parent[x]);
    }
    public static void union(int x, int y){
        x= find(x);
        y = find(y);
        if(x!=y){
            parent[x] = y;
        }
    }
}
