import java.io.*;
import java.util.*;

public class Main {
	static StringBuilder sb=new StringBuilder();
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;


		st=new StringTokenizer(br.readLine());
		
		int N=Integer.parseInt(st.nextToken());
		int K=Integer.parseInt(st.nextToken());
		
		Queue<Integer> [] queue=new LinkedList[101];
		
		for(int i=1;i<=100;i++) 
			queue[i]=new LinkedList<>();
		
		HashSet<Integer> isMoving=new HashSet<>();
		
		
		st=new StringTokenizer(br.readLine());
		
		int arr[]=new int[K]; 
		for(int i=0;i<K;i++) { 
			arr[i]=Integer.parseInt(st.nextToken());
			queue[arr[i]].add(i);
		}
		
		
		int i=0;
		for(i=0;i<K;i++) {
			isMoving.add(arr[i]);
			queue[arr[i]].poll();
			if(isMoving.size()==N) {
				i++;
				break;
			}
			
		}
		
		int count=0;
		
		for(;i<K;i++) {
			int num=arr[i];
			queue[num].poll();
			int index= -1;
			int max=0;
			if(isMoving.contains(num))
				continue;
			for(int val:isMoving) {
				if(queue[val].isEmpty()) { 
					index=val;
					break;
				}
				if(queue[val].peek()>max) {
					max=queue[val].peek();
					index=val;
				}
			}
			
			isMoving.remove(index);
			isMoving.add(num);
			count++;
			
		}
		
		
		System.out.println(count);
		
		
		

	}
}