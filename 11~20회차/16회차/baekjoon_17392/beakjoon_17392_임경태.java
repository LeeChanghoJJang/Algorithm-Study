// 17392 우울한 방학
import java.io.*;
import java.util.*;

public class beakjoon_17392 {
    // 입력과 출력 설정
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws Exception {
        // 첫 번째 줄에서 N과 M을 입력받음
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // 배열을 선언하고, 두 번째 줄에서 N개의 정수를 입력받음
        st = new StringTokenizer(br.readLine());
        int[] arr = new int[N];
        int notBlue = 0;

        // 입력받은 N개의 정수를 배열에 저장하고 합계를 계산
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            notBlue += arr[i] + 1;
        }

        // 주어진 M에서 notBlue 뺀 값을 blue에 저장
        int blue = M - notBlue;
        int ans = 0;

        // blue가 0보다 큰 경우 추가 계산 진행
        if (blue > 0) {
            int mood = 1;
            // b를 (N + 1)로 나눈 몫이 0이 아닐 동안 반복
            while (blue / (N+1) != 0) {
                ans += Math.pow(mood, 2) * (N+1);
                blue -= (N+1);
                mood++;
            }
            // 놀러가는 날 + 1 의 기회가 있다
            ans += Math.pow(mood, 2) * (blue % (N+1));
        }

        // 최종 결과 출력
        bw.write(ans + "\n");

        // 입출력 닫기
        bw.flush();
        br.close();
        bw.close();
    }
}
