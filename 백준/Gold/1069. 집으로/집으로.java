import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int X = Integer.parseInt(st.nextToken());
        int Y = Integer.parseInt(st.nextToken());
        int D = Integer.parseInt(st.nextToken());
        int T = Integer.parseInt(st.nextToken());
        int cx=0; int cy=0;
        double dist = (Math.sqrt(Math.pow(X-cx,2)+Math.pow(Y-cy,2))); //대각선 거리
        if(T>=D){
            System.out.println(dist);
            return;
        }
        //T<D인 경우
        double time = 0;
        while(dist>0){
            if(dist>=2*D){
                time += T;
                dist -= D;
            }
            else{
                double triangle = 2*T;
                double jump_num = Math.ceil(dist/D);
                double jump_back = jump_num*T + (D*jump_num - dist); //점프했다가 되돌아옴
                double jump_straight = (jump_num-1)*T + dist - D*(jump_num-1); //점프하고 직선으로 가는 경우
                double straight = dist; //직선으로 가는 경우
                time += Math.min(jump_straight,Math.min(triangle,Math.min(jump_back, straight)));
                dist = 0;
            }
        }
        System.out.println(time);

    }


}
