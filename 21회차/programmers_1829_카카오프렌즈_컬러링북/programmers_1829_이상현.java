import java.util.Stack;

class Solution {
    public int dfs(int r, int c, int m, int n, boolean[][] visited, int[][] picture) {
        Stack<int[]> stack = new Stack<>();
        stack.push(new int[]{r, c});
        visited[r][c] = true;
        int size = 1;
        int[] dr = {1, 0, -1, 0};
        int[] dc = {0, 1, 0, -1};
        
        while (!stack.isEmpty()) {
            int[] cur = stack.pop();
            int cr = cur[0];
            int cc = cur[1];
            
            for (int i = 0; i < 4; i++) {
                int nr = cr + dr[i];
                int nc = cc + dc[i];
                
                if (0 <= nr && nr < m && 0 <= nc && nc < n && !visited[nr][nc] && picture[cr][cc] == picture[nr][nc]) {
                    visited[nr][nc] = true;
                    stack.push(new int[]{nr, nc});
                    size++;
                }
            }
        }
        
        return size;
    }
    
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        int[] answer = new int[2];
        
        boolean[][] visited = new boolean[m][n];
        
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (!visited[r][c] && picture[r][c] != 0) {
                    numberOfArea++;
                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea, dfs(r, c, m, n, visited, picture));
                }
            }
        }
        
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        
        return answer;
    }
}
