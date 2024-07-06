import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static char[][] map;
    static int[][] visit;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};
    static char[] direction = {'L', 'R', 'U', 'D'};
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new char[N][M];
        visit = new int[N][M];
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                map[i][j] = line.charAt(j);
                visit[i][j] = -1; // 초기값 -1
            }
        }

        int idx = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (visit[i][j] == -1) {
                    move(i, j, idx);
                    idx++;
                }
            }
        }

        System.out.println(answer);
    }

    public static void move(int x, int y, int idx) {
        if (visit[x][y] != -1) { // 방문한 경우
            if (visit[x][y] == idx) {
                answer++;
            }
            return;
        }

        visit[x][y] = idx; // 현재 탐색 인덱스로 마크
        int i = 0;
        for (; i < 4; i++) {
            if (map[x][y] == direction[i]) {
                break;
            }
        }

        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
            move(nx, ny, idx);
        }
    }
}
