import java.util.*;

class Solution {
    static int[][] dr = new int[][] {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    static boolean[][] visited;
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        
        visited = new boolean[m][n];
        List<Integer> areas = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (picture[i][j] != 0 && !visited[i][j]) {
                    areas.add(bfs(i, j, m, n, picture));
                }
            }
        }
        
        numberOfArea = areas.size();
        maxSizeOfOneArea = Collections.max(areas);
        
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
    public static int bfs(int x, int y, int m, int n, int[][] picture) {
        Queue<int[]> que = new LinkedList<>();
        que.add(new int[]{x, y});
        visited[x][y] = true;
        int color = picture[x][y];
        int cnt = 0;
        while (!que.isEmpty()) {
            int[] cur = que.poll();
            cnt++;

            for (int d = 0; d < 4; d++) {
                int nx = cur[0] + dr[d][0];
                int ny = cur[1] + dr[d][1];
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && picture[nx][ny] == color && !visited[nx][ny]) {
                    que.offer(new int[]{nx, ny});
                    visited[nx][ny] = true;
                }
            }
        }
        return cnt;
    }
}