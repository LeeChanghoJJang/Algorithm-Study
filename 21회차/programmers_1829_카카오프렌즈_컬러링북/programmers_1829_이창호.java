import java.util.*;

class Solution {
    static boolean[][] visit;
    static int[][] map;
    static List<Integer> list;
    static int N, M;
    public int[] solution(int m, int n, int[][] picture) {
        N = n;
        M = m;
        map = picture;
        list = new ArrayList();
        visit = new boolean[m][n];

        for(int i = 0 ; i < m; ++i){
            for(int j = 0 ; j < n; ++j){
                if(!visit[i][j] && map[i][j] != 0){
                    search(i,j);
                }
            }
        }

        int[] answer = new int[2];
        answer[0] = list.size();
        answer[1] = list.stream().max(Integer::compare).get();

        return answer;
    }

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public void search(int startX, int startY){
        int count = 1;
        visit[startX][startY] = true;
        Queue<int[]> q = new ArrayDeque();
        q.add(new int[] {startX, startY});
        while(!q.isEmpty()){
            int[] cur = q.poll();
            for(int d = 0; d < 4; ++d){
                int nextX = cur[0] + dx[d];
                int nextY = cur[1] + dy[d];
                if(0 <= nextX && nextX < M && 0 <= nextY && nextY < N){
                    if(!visit[nextX][nextY] && map[nextX][nextY] == map[startX][startY]){
                        visit[nextX][nextY] = true;
                        q.add(new int[] {nextX, nextY});
                        count++;
                    }
                }
            }
        }
        list.add(count);
    }
}