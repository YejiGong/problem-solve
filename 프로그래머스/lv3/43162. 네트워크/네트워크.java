import java.util.*;
class Solution {
    int[] visited;
    public int solution(int n, int[][] computers) {
        visited = new int[n];
        int answer = 0;
        for(int i=0; i<n; i++){
            if(visited[i] == 0 ){
                bfs(computers, visited, i, n);
                answer+=1;
            }
        }
        return answer;
    }
    public void bfs(int[][] computers, int[] visited, int x, int n){
        visited[x]=1;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(x);
        while(queue.size()>0){
            int tmp = queue.poll();
            for(int i=0; i<n; i++){
                if(i!=tmp && computers[tmp][i]==1 && visited[i]==0){
                    visited[i] = 1;
                    queue.add(i);
                }
            }
        }
    }
}