import java.util.*;
import java.awt.Point;
class Solution {
    int[] dx={-1,0,1,0};
    int[] dy={0,1,0,-1};
    int[][] visited;
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        visited=new int[n][m];
        bfs(maps, visited, 0, 0, n, m);
        int answer = visited[n-1][m-1];
        if(answer==0){
            return -1;
        }else{
            return answer;
        }
    }
    public void bfs(int[][] maps, int[][] visited, int x, int y, int n, int m){
        Queue<Point> queue = new LinkedList<>();
        queue.add(new Point(x,y));
        visited[x][y] = 1;
        while(queue.size()>0){
            Point p = queue.poll();
            for(int i=0; i<4; i++){
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];
                if(0<=nx && nx<n && 0<=ny && ny<m && maps[nx][ny]==1 && visited[nx][ny]==0){
                    visited[nx][ny]=visited[p.x][p.y]+1;
                    queue.add(new Point(nx,ny));
                }
            }
        }
    }
    
}