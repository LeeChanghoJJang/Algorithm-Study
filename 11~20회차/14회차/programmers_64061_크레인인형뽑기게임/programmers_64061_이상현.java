import java.util.ArrayDeque;

class Solution {
	static ArrayDeque<Integer> stack = new ArrayDeque<>();
	
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        int height = board[0].length;
        
        for (int i = 0; i < moves.length; i++) {
        	int j = 0;
        	while (j < height && board[j][moves[i] - 1] == 0) j++;
        	if (j == height) continue;
        	
        	if (!stack.isEmpty() && stack.peek() == board[j][moves[i] - 1]) {
        		stack.pop();
        		answer += 2;
        	} else {
        		stack.push(board[j][moves[i] - 1]);
        	}
        	board[j][moves[i] - 1] = 0;
        }
        
				
        return answer;
    }
}