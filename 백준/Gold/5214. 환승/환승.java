import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static class Node {
		int v, move;
		Node (int v, int move) {
			this.v = v;
			this.move = move;
		}
	}
	
	static int N, K, M;
	static List<Integer>[] hypertubes, stations;
	
	public static void main(String[] args) {
		try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
				BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out))) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			
			hypertubes = new ArrayList[M + 1];
			stations = new ArrayList[N + 1];
			for (int i = 0; i <= M; ++i) hypertubes[i] = new ArrayList<>();
			for (int i = 0; i <= N; ++i) stations[i] = new ArrayList<>();
			for (int i = 1; i <= M; ++i) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < K; ++j) {
					int station = Integer.parseInt(st.nextToken());
					hypertubes[i].add(station);
					stations[station].add(i);
				}
			}
			if (N == 1) bw.write(1 + "\n");
			else bw.write(bfs() + "\n");
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public static int bfs() {
		boolean[] visitHT = new boolean[M + 1];
		boolean[] visitS = new boolean[N + 1];
		Queue<Node> q = new LinkedList<>();
		visitS[1] = true;
		for (int v : stations[1]) {
			visitHT[v] = true;
			q.offer(new Node(v, 1));
		}
		
		while (!q.isEmpty()) {
			Node n = q.poll();
			for (int v : hypertubes[n.v]) {
				if (v == N) return n.move + 1;
				if (visitS[v]) continue;
				visitS[v] = true;
				for (int nv : stations[v]) {
					if (visitHT[nv]) continue;
					visitHT[nv] = true;
					q.offer(new Node(nv, n.move + 1));
				}
			}
		}
		return -1;
	}
}