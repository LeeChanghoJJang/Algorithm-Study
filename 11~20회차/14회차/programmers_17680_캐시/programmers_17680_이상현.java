import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        Queue<String> q = new LinkedList<>();
        HashSet<String> set = new HashSet<>();
        
        if (cacheSize == 0) {
            return 5 * cities.length;
        }
        
        for (int i = 0; i < cities.length; i++) {
            cities[i] = cities[i].toLowerCase();

            if (q.size() < cacheSize) {
                if (set.contains(cities[i])) {
                    answer += 1;
                    q.remove(cities[i]);
                    q.add(cities[i]);
                } else {
                    answer += 5;
                    q.add(cities[i]);
                    set.add(cities[i]);
                }
            } else {
                if (set.contains(cities[i])) {
                    answer += 1;
                    q.remove(cities[i]);
                    q.add(cities[i]);
                } else {
                    answer += 5;
                    set.remove(q.poll());
                    q.add(cities[i]);
                    set.add(cities[i]);
                }
            }
        }

        return answer;
    }
}