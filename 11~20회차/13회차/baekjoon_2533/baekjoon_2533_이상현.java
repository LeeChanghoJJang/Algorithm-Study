import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.io.IOException;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int[][] dp; // dp 배열은 각 노드에서의 최적해를 저장합니다. dp[i][0]은 i번째 노드가 얼리 어댑터가 아닐 때, dp[i][1]은 i번째 노드가 얼리 어댑터일 때의 최적해를 저장합니다.
    static List<List<Integer>> graph; // 각 노드와 그에 인접한 노드들의 정보를 저장하는 그래프입니다.
    static boolean[] visited; // 방문 여부를 저장하는 배열입니다. 해당 노드를 방문했는지를 확인합니다.

    static void dfs(int vertex) throws IOException {
        for (int v: graph.get(vertex)) { // 각 노드의 인접한 노드들을 방문합니다.
            if (visited[v]) { // 이미 방문한 노드라면 넘어갑니다.
                continue;
            }

            visited[v] = true; // 해당 노드를 방문했다고 표시합니다.
            dfs(v); // 해당 노드를 시작으로 DFS를 재귀적으로 호출합니다.
            dp[vertex][0] += dp[v][1]; // 현재 노드가 얼리 어댑터가 아닐 때, 자식 노드들이 얼리 어댑터일 때의 최적해를 더합니다.
            
            if (dp[v][0] < dp[v][1]) { // 자식 노드가 얼리 어댑터일 때와 아닐 때 중 최적해를 선택하여 현재 노드의 최적해를 갱신합니다.
                dp[vertex][1] += dp[v][0];
            } else {
                dp[vertex][1] += dp[v][1];
            }
        }
    }

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine()); // 노드의 개수를 입력받습니다.
        dp = new int[N + 1][2]; // dp 배열을 초기화합니다.
        graph = new ArrayList<>(); // 그래프를 초기화합니다.
        visited = new boolean[N + 1]; // 방문 여부를 저장하는 배열을 초기화합니다.

        for (int i = 0; i < N + 1; i++) { // 그래프의 각 노드에 대해 인접한 노드들을 저장할 ArrayList를 초기화합니다.
            graph.add(new ArrayList<>());
        }
        
        for (int i = 0; i < N + 1; i++) { // dp 배열의 모든 요소를 초기값으로 설정합니다.
            dp[i][1] = 1; // 어댑터가 아닐 때의 최적해를 1로 설정합니다. (자기 자신만 얼리 어댑터가 될 수 있는 경우를 고려하여 초기값을 1로 설정합니다.)
        }

        for (int i = 0; i < N - 1; i++) { // 그래프의 간선 정보를 입력받아 인접 리스트를 구성합니다.
            String[] inputs = br.readLine().split(" ");
            int u = Integer.parseInt(inputs[0]);
            int v = Integer.parseInt(inputs[1]);
            graph.get(u).add(v); // 양방향 그래프이므로 각 노드의 인접 리스트에 상대 노드를 추가합니다.
            graph.get(v).add(u);
        }

        visited[1] = true; // 루트 노드인 1번 노드를 방문했다고 표시합니다.
        dfs(1); // DFS 탐색을 시작합니다.
        
        if (dp[1][0] < dp[1][1]) { // 루트 노드가 얼리 어댑터가 아닐 때와 얼리 어댑터일 때 중에서 최적해를 선택하여 출력합니다.
            bw.write(Integer.toString(dp[1][0]));
        } else {
            bw.write(Integer.toString(dp[1][1]));
        }
        
        bw.flush(); // BufferedWriter를 비워줍니다.
        bw.close(); // BufferedWriter를 닫아줍니다.
        br.close(); // BufferedReader를 닫아줍니다.
    }
}
