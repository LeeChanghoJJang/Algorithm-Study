import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static List<int[]> arr = new ArrayList<>();
    static List<int[]> dp = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int a, b, c, A, B, C;
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        A = a; B = b; C = c;

        for (int i = 1; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x, y, z;
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());
            z = Integer.parseInt(st.nextToken());
            int AB = Math.max(A, B);
            int BC = Math.max(B, C);
            int ABC = Math.max(AB, BC);
            int ab = Math.min(a, b);
            int bc = Math.min(b, c);
            int abc = Math.min(ab, bc);

            A = x + AB;
            B = y + ABC;
            C = z + BC;

            a = x + ab;
            b = y + abc;
            c = z + bc;
        }

        int maxScore = Math.max(A, Math.max(B, C));
        int minScore = Math.min(a, Math.min(b, c));
        System.out.println(maxScore + " " + minScore);
    }
}