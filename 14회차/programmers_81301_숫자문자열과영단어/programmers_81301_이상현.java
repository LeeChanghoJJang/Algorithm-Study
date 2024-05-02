import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;

class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static String[] arr = new String[] {
    		"zero", "one", "two", "three", "four", 
    		"five", "six", "seven", "eight", "nine"
    	};
    public int solution(String s) {
        for (int i = 0; i < 10; i++) {
    		s = s.replaceAll(arr[i], Integer.toString(i));
    	}
        int answer = Integer.parseInt(s);
        return answer;
    }
}