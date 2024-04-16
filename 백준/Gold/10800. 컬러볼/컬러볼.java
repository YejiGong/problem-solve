import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static class Ball implements Comparable<Ball>{
        int C;
        int S;
        int num;
        public Ball(int C, int S, int num){
            this.C = C;
            this.S = S;
            this.num = num;
        }
        @Override
        public int compareTo(Ball o){
            return this.S - o.S;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.valueOf(br.readLine());
        Ball[] arr = new Ball[N];
        for(int i=0; i<N; i++){
            String[] input = br.readLine().split(" ");
            int C = Integer.valueOf(input[0]);
            int S = Integer.valueOf(input[1]);
            arr[i] = new Ball(C,S,i);
        }
        int[] result = new int[N];
        HashMap<Integer, Integer> balls = new HashMap<>();
        Arrays.sort(arr);
        int total = 0;
        int prevS = 0;
        int prevTotal = 0;
        int prevPoint = 0;
        for(int i=0; i<N; i++){
            Ball ball = arr[i];
            if(prevS != ball.S) {
                if(i!=0) {
                    prevTotal = total;
                    for (int j = prevPoint; j < i; j++) {
                        balls.put(arr[j].C, balls.getOrDefault(arr[j].C, 0) + arr[j].S);
                    }
                    prevPoint = i;
                }

                result[ball.num] = total - balls.getOrDefault(ball.C, 0);
            }else{
                result[ball.num] = prevTotal - balls.getOrDefault(ball.C, 0);
            }
            total += ball.S;
            prevS = ball.S;
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for(int i=0; i<N; i++){
            bw.write(String.valueOf(result[i]));
            bw.newLine();
        }
        bw.close();
    }

}
