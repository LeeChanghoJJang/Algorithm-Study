import java.util.*;

public class Solution {
	static Stack<Integer> stack = new Stack<>();
	
    public int[] solution(int []arr) {
        int n = arr.length;
        
        for (int i = 0; i < n; i++) {
        	if (stack.isEmpty()) {
        		stack.push(arr[i]);
        	} else {
        		if (stack.peek() != arr[i]) {
        			stack.push(arr[i]);
        		}
        	}
        }
        
        int[] answer = stack.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}