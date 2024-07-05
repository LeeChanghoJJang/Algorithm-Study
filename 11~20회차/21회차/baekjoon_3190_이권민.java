import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        int K = Integer.parseInt(br.readLine());
        int[][] matrix = new int [N+1][N+1];
        int count = 0;
        for (int i = 0;i<K;i++) {
            st = new StringTokenizer(br.readLine());
            matrix[Integer.parseInt(st.nextToken())][Integer.parseInt(st.nextToken())] = 1;

        }
        int L = Intger.parseInt(br.readLine());
        for (int i = 0; i < L; i++) {
            st = new StringTokenizer(br.readLine());
            int second = Integer.parseInt(st.nextToken());
            char direcion = st.nextToken();
            if (direcion == 'L') {

            } else {

            }
        }
    }
}
//visited로 head랑 tail만 갱신?
//따로 함수 만들어서 L 친구들 받고 second전까지 돌리고.deque로 앞에 더하고 뒤에 뺴면 되네.
//게임 오버되는 건 밖으로 나가거나 deque안에 있는지 체크(가 오래걸릴거같은데) 그냥 visited안되나.