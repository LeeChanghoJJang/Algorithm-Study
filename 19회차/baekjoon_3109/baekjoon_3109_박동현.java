package bj_3109;

import java.io.*;
import java.util.*;

public class Main {
    // dr 델타
    static int[][] dr = {
            {-1,1},
            {0,1},
            {1,1}
    };
    static int cnt = 0;
    static int N ;
    static int M ;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st ;
        // N,M
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        // arr
        char[][] arr = new char[N][M];
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            String data = st.nextToken();
            for (int j=0; j<data.length(); j++) {
                arr[i][j] = data.charAt(j);
            }
        }

        // System.out.println(Arrays.deepToString(arr));
        for (int i=0; i<N; i++) {
            dfs(arr, i, 0);
        }
        System.out.println(cnt);
    }
    public static boolean dfs(char[][] arr, int x, int y) {
        if (y==M-1) {
            cnt ++;
            return true;
        }

        for (int[] d : dr) {
            int di = x+d[0];
            int dj = y+d[1];

            if (0<= di && di < N && 0 <= dj && dj < M && arr[di][dj] == '.') {
                arr[di][dj] = 'x';
                if (dfs(arr,di,dj)) {
                    return true;
                }
            }
        }
        return false;
    }
}
