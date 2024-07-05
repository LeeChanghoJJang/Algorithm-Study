import java.io.*;
import java.util.*;

public class Main {
    static int N, K, L;
    static int[][] matrix;
    static int[][] directions = {{0,1}, {1,0}, {0,-1}, {-1,0}}; // Right, Down, Left, Up
    static Map<Integer, Character> commandMap = new HashMap<>();
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        K = Integer.parseInt(br.readLine());
        matrix = new int[N+1][N+1];
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            matrix[r][c] = 1; // Apple
        }
        L = Integer.parseInt(br.readLine());
        for (int i = 0; i < L; i++) {
            st = new StringTokenizer(br.readLine());
            int second = Integer.parseInt(st.nextToken());
            char direction = st.nextToken().charAt(0);
            commandMap.put(second, direction);
        }

        System.out.println(playGame());
    }

    static int playGame() {
        Deque<int[]> snake = new LinkedList<>();
        snake.offer(new int[]{1, 1});
        boolean[][] visited = new boolean[N+1][N+1];
        visited[1][1] = true;
        int time = 0;
        int directionIndex = 0; // Starting direction is 'Right'

        while (true) {
            time++;
            int[] head = snake.peekFirst();
            int nextRow = head[0] + directions[directionIndex][0];
            int nextCol = head[1] + directions[directionIndex][1];

            // Check if the snake hits the wall or itself
            if (nextRow <= 0 || nextRow > N || nextCol <= 0 || nextCol > N || visited[nextRow][nextCol]) {
                return time;
            }

            // Move the snake
            if (matrix[nextRow][nextCol] == 1) {
                // Eat the apple
                matrix[nextRow][nextCol] = 0; // Remove the apple
            } else {
                // Move the tail
                int[] tail = snake.pollLast();
                visited[tail[0]][tail[1]] = false;
            }

            // Add new head position
            snake.offerFirst(new int[]{nextRow, nextCol});
            visited[nextRow][nextCol] = true;

            // Change direction if needed
            if (commandMap.containsKey(time)) {
                char turn = commandMap.get(time);
                if (turn == 'L') {
                    directionIndex = (directionIndex + 3) % 4; // Turn left
                } else {
                    directionIndex = (directionIndex + 1) % 4; // Turn right
                }
            }
        }
    }
}
