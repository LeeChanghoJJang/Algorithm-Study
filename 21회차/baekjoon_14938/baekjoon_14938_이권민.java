import java.io.*;
import java.util.*;
public class Main {
    //BFS 지역 이동 정보 클래스
    static class node implements Comparable<node>{
        // 이 노드 객체를 다른 노드객체와 비교할 수 있다.
        // Comparable 인터페이스를 구현하면 compareTo메서드를 만들어야 함
        int position, value;
        public node(int position, int value) {
            this.position = position;
            this.value = value;
        }
        //거리 기준 오름차순 정렬
        // @Override
        public int compareTo(node o) {
            return this.value - o.value;
        }
    }
    static int answer = Integer.MIN_VALUE;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int[] score = new int[n+1];
        ArrayList<ArrayList<node>> graph = new ArrayList<>();
        for(int i=0;i<=n;i++)
            graph.add(new ArrayList<>());

        st = new StringTokenizer(br.readLine());
        //각 지역 아이템 개수 배열에 저장
        for(int i=1;i<=n;i++)
            score[i] = Integer.parseInt(st.nextToken());
        //양방향 길에 대한 정보 저장
        for(int i=0;i<r;i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int l = Integer.parseInt(st.nextToken());

            graph.get(a).add(new node(b, l));
            graph.get(b).add(new node(a, l));
        }
        //각 지역에서 출발했을 때 최대로 먹을 수 있는 아이템 탐색
        for(int i=1;i<=n;i++)
            answer = Math.max(search(i, graph, score, n, m), answer);

        System.out.println(answer);
        br.close();
    }
    //BFS탐색을 통해 각 지역에서 탐색범위 안에 먹을 수 있는 아이템 개수 탐색하는 함수
    static int search(int start, ArrayList<ArrayList<node>> graph, int[] score, int size, int max) {
        PriorityQueue<node> q = new PriorityQueue<>();
        boolean[] visited = new boolean[size+1];
        q.add(new node(start, 0));	//출발 지역 저장
        int result = 0;		//먹은 아이템 개수
        //탐색 진행!
        while(!q.isEmpty()) {
            node cur = q.poll();
            if(visited[cur.position] == true)	//이미 최단 거리로 방문한 경우
                continue;
            result += score[cur.position];	//해당 지역 아이템 개수 증가
            visited[cur.position] = true;	//해당 지역 방문 확인
            //인접한 길 탐색!
            for(node next : graph.get(cur.position)) {
                if(!visited[next.position] && max - (cur.value + next.value) >= 0) {
                    q.add(new node(next.position, cur.value + next.value));
                }
            }
        }
        return result;		//먹은 아이템 개수 반환

    }
}