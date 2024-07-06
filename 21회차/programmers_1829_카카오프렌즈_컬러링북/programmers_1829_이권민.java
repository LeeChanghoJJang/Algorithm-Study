import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};

    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;  // 영역의 수
        int maxSizeOfOneArea = 0;  // 가장 큰 영역의 크기

        boolean[][] visited = new boolean[m][n];  // 방문 여부를 확인하는 배열

        // 모든 셀을 순회하면서 새로운 영역을 발견하면 BFS를 수행
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (picture[i][j] != 0 && !visited[i][j]) {
                    numberOfArea++;  // 새로운 영역 발견
                    int sizeOfArea = bfs(i, j, m, n, picture, visited);  // 영역의 크기 계산
                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea, sizeOfArea);  // 가장 큰 영역의 크기 업데이트
                }
            }
        }

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }

    // BFS 알고리즘을 사용하여 영역의 크기를 계산
    public int bfs(int r, int c, int M, int N, int[][] picture, boolean[][] visited) {
        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{r, c});
        visited[r][c] = true;
        int color = picture[r][c];
        int count = 0;

        // 큐가 빌 때까지 반복
        while (!queue.isEmpty()) {
            int[] point = queue.poll();
            int row = point[0];
            int col = point[1];
            count++;

            // 4방향으로 인접한 셀을 검사
            for (int i = 0; i < 4; i++) {
                int nx = row + dx[i];
                int ny = col + dy[i];

                // 범위 내에 있고, 같은 색상이며, 방문하지 않은 셀만 큐에 추가
                if (nx >= 0 && nx < M && ny >= 0 && ny < N && picture[nx][ny] == color && !visited[nx][ny]) {
                    queue.add(new int[]{nx, ny});
                    visited[nx][ny] = true;
                }
            }
        }
        return count;  // 영역의 크기를 반환
    }
}
