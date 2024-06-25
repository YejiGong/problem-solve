import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for(int i=0; i<N; i++) {
            String input = br.readLine();
            if (input.length() >= 6 && input.length() <= 9) {
                System.out.println("yes");
            } else {
                System.out.println("no");
            }
        }
        
    }
}

