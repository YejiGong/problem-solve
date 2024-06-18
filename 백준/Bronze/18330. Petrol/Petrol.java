import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());
        k+=60;
        if(N-k>0){
            System.out.println(k*1500+(N-k)*3000);
        }else{
            System.out.println(N*1500);
        }
    }


}

