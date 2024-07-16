import java.io.*;
import java.math.BigInteger;
import java.util.*;
import java.lang.Math;

public class Main {
    public static class Node{
        long data;
        long newData;
        public Node(long data){
            this.data = data;
        }
        public void update(long newData){
            this.newData = newData;
        }
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        Long[] nums = new Long[N];
        for(int i=0; i<N; i++){
            long tmp = Long.parseLong(st.nextToken());
            nums[i] = tmp;
        }
        Arrays.sort(nums, (a, b) -> {
            BigInteger ab = new BigInteger(String.valueOf(a) + String.valueOf(b));
            BigInteger ba = new BigInteger(String.valueOf(b) + String.valueOf(a));
            return ba.compareTo(ab);
        });
        String result = "";
        for(int i=0; i<N; i++){
            result += String.valueOf(nums[i]);
        }
        if(result.substring(0,1).equals("0")){
            System.out.println("0");
        }else{
            System.out.println(result);
        }

    }


}

