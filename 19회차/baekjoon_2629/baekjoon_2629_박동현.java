package bj_2629;

import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st ;


        // N
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        // chu
        st = new StringTokenizer(br.readLine());
        int[] chu = new int[N];
        for (int i=0; i<N; i++) {
            chu[i] = Integer.parseInt(st.nextToken());
        }

        // M
        st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        // target
        st = new StringTokenizer(br.readLine());
        int[] target = new int[M];
        for (int i=0; i<M; i++) {
            target[i] = Integer.parseInt(st.nextToken());
        }
        // dp
        Set<Integer> dp = new HashSet<>();
        dp.add(0);
        for (int weight : chu) {
            Set<Integer> tmp = new HashSet<>();
            for (int i : dp) {
                tmp.add(i+weight);
                tmp.add(Math.abs(i-weight));
            }
            dp.addAll(tmp);
        }
        // 출력
        for (int t: target) {
            if(dp.contains(t)) {
                System.out.println("Y");
            } else {
                System.out.println("N");
            }
        }
    }
}
