// 1829 카카오 프렌즈 컬러링북
import java.util.*;

class Solution {
    public int[] solution(int m, int n, int[][] picture) {
        int[] di = {0, 1, 0, -1};
        int[] dj = {1, 0, -1, 0};
        
        boolean[][] visit = new boolean[m][n];
        int[] ans = {0, 0};

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (picture[i][j] != 0 && !visit[i][j]) {
                    visit[i][j] = true;
                    ans[1] = Math.max(ans[1], bfs(i, j, picture[i][j], m, n, picture, visit, di, dj));
                    ans[0]++;
                }
            }
        }
        return ans;
    }

    private static int bfs(int ci, int cj, int color, int m, int n, int[][] picture, boolean[][] visit, int[] di, int[] dj) {
        Queue<int[]> Q = new LinkedList<>();
        Q.add(new int[]{ci, cj});
        int area = 1;

        while (!Q.isEmpty()) {
            int[] curr = Q.poll();
            int i = curr[0], j = curr[1];

            for (int d = 0; d < 4; d++) {
                int ni = i + di[d];
                int nj = j + dj[d];

                if (ni >= 0 && ni < m && nj >= 0 && nj < n && !visit[ni][nj] && picture[ni][nj] == color) {
                    Q.add(new int[]{ni, nj});
                    visit[ni][nj] = true;
                    area++;
                }
            }
        }
        return area;
    }
}