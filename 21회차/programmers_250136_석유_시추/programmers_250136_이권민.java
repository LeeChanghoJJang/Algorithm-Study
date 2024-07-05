import java.util.*;

class Solution {
    static int[] dr = {0, 1, 0, -1};
    static int[] dc = {1, 0, -1, 0};

    public int solution(int[][] land) {
        int[][] visited = new int[land.length][land[0].length];
        HashMap<Integer, Integer> zoneCount = new HashMap<>(); // HashMap으로 각 영역 번호와 크기 저장
        int zoneNum = 1;

        for (int i = 0; i < land.length; i++) {
            for (int j = 0; j < land[0].length; j++) {
                if (land[i][j] == 1 && visited[i][j] == 0) {
                    int zoneSize = bfs(i, j, zoneNum, land, visited);
                    zoneCount.put(zoneNum, zoneSize);
                    zoneNum += 1;
                }
            }
        }

        int maxNum = 0;
        for (int j = 0; j < land[0].length; j++) {
            HashSet<Integer> zoneCheck = new HashSet<>();
            int cntNum = 0;
            for (int i = 0; i < land.length; i++) {
                if (visited[i][j] != 0 && !zoneCheck.contains(visited[i][j])) {
                    zoneCheck.add(visited[i][j]);
                    cntNum += zoneCount.get(visited[i][j]);
                }
            }
            maxNum = Math.max(maxNum, cntNum);
        }

        return maxNum;
    }

    public int bfs(int r, int c, int zoneNum, int[][] land, int[][] visited) {
        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{r, c});
        visited[r][c] = zoneNum;
        int count = 1;

        while (!q.isEmpty()) {
            int[] oilzone = q.poll();
            for (int i = 0; i < 4; i++) {
                int lr = oilzone[0] + dr[i];
                int lc = oilzone[1] + dc[i];
                if (lr >= 0 && lr < land.length && lc >= 0 && lc < land[0].length && land[lr][lc] == 1 && visited[lr][lc] == 0) {
                    count += 1;
                    q.add(new int[]{lr, lc});
                    visited[lr][lc] = zoneNum;
                }
            }
        }
        return count;
    }
}
