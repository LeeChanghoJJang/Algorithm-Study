import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int[] list_;
    static int[][] seg; // 세그먼트 트리 배열

    // 세그먼트 트리 초기화 함수
    static int[] init(int i, int start, int end) {
        if (start == end) {
            seg[i] = new int[]{list_[start], list_[start]}; // 리프 노드 설정
            return seg[i];
        }

        int mid = (start + end) / 2;
        int[] l = init(i * 2, start, mid); // 왼쪽 자식 노드 초기화
        int[] r = init(i * 2 + 1, mid + 1, end); // 오른쪽 자식 노드 초기화
        seg[i] = new int[]{Math.min(l[0], r[0]), Math.max(l[1], r[1])}; // 현재 노드의 값 설정

        return seg[i];
    }

    // 구간에 대한 최소값과 최대값을 찾는 함수
    static int[] find(int start, int end, int i, int a, int b) {
        if (end < a || b < start) {
            return new int[]{(int) 1e9, 0}; // 범위가 구간을 벗어날 때 초기값 반환
        }

        int mid = (start + end) / 2;

        if (a <= start && end <= b) {
            return seg[i]; // 현재 구간이 찾는 구간에 완전히 포함될 때 현재 노드의 값 반환
        } else {
            int[] l = find(start, mid, i * 2, a, b); // 왼쪽 자식 노드에서 탐색
            int[] r = find(mid + 1, end, i * 2 + 1, a, b); // 오른쪽 자식 노드에서 탐색
            return new int[]{Math.min(l[0], r[0]), Math.max(l[1], r[1])}; // 자식 노드들의 결과 병합
        }
    }

    public static void main(String[] args) throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()); // 배열의 크기
        int M = Integer.parseInt(st.nextToken()); // 질의의 개수
        list_ = new int[N]; // 배열 초기화
        seg = new int[4 * N][2]; // 세그먼트 트리 배열 초기화

        // 배열의 값 입력
        for (int i = 0; i < N; i++) {
            list_[i] = Integer.parseInt(br.readLine());
        }

        // 세그먼트 트리 초기화
        init(1, 0, list_.length - 1);

        // 질의에 대한 답 출력
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1; // 질의의 시작 인덱스
            int b = Integer.parseInt(st.nextToken()) - 1; // 질의의 끝 인덱스
            int[] ans = find(0, list_.length - 1, 1, a, b); // 질의에 대한 답 찾기
            bw.write(ans[0] + " " + ans[1] + "\n"); // 최소값과 최대값 출력
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
