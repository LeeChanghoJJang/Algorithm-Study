import java.util.LinkedList;
import java.util.Queue;

class Solution {
    static int[][] dr = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    public static int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        int[][] visit = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (picture[i][j] != 0 && visit[i][j] == 0) {
                    int target = picture[i][j];
                    Queue<int[]> q = new LinkedList<>();
                    q.offer(new int[]{i, j});
                    visit[i][j] = 1;
                    int cnt = 1;

                    while (!q.isEmpty()) {
                        int[] current = q.poll();
                        int x = current[0];
                        int y = current[1];

                        for (int[] direction : dr) {
                            int di = x + direction[0];
                            int dj = y + direction[1];
                            if (0 <= di && di < m && 0 <= dj && dj < n && visit[di][dj] == 0 && picture[di][dj] == target) {
                                cnt++;
                                visit[di][dj] = 1;
                                q.offer(new int[]{di, dj});
                            }
                        }
                    }
                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea, cnt);
                    numberOfArea++;
                }
            }
        }
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
}