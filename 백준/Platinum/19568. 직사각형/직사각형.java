import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        //BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[][] arr = new int[30][30];
        for(int i=0; i<30; i++){
            for(int j=0; j<30; j++){
                if(i==15 && j<15){
                    arr[i][j] = 1;
                }else if(i==15 && j>15){
                    arr[i][j] = 15;
                }else if(i<15 && j==15){
                    arr[i][j] =225;
                }else if(i>15 && j==15){
                    arr[i][j] = 3375;
                }else{
                    arr[i][j]= 0;
                }

            }
        }

        for(int i=0; i<30; i++){
            for(int j=0; j<30; j++){
                System.out.print(arr[i][j]+" ");
            }
            System.out.println("");
        }

    }
}

