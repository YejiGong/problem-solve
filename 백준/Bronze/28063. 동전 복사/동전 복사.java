import java.util.Scanner;

public class Main {
    static int N;
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt();
        int x = scanner.nextInt();
        int y = scanner.nextInt();
        if(N==1){
            System.out.println(0);
        }
        else if((x==1|| x==N) && (y==1 || y==N)){
            System.out.println(2);
        }
        else if(x==1 || x==N || y==1 || y==N) {
            System.out.println(3);
        }else{
            System.out.println(4);
        }

    }

}
