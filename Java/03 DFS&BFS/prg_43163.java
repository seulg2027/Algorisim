/**
 * prg_43163
 */
import java.util.*;

public class prg_43163 {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        int n = words.length;
        
        Queue<List> q = new LinkedList<>();
        q.add(Arrays.asList(begin, 0)); // List 넣을 때
        boolean[] visited = new boolean[n];
        
        while (!q.isEmpty()) {
            List<?> now = q.poll();
            String cmp_char = (String)now.get(0); // List에서 인덱스로 가져올 때
            int cmp_cnt = (int)now.get(1);
            
            if (now.get(0).equals(target)) {
                answer = cmp_cnt;
                break;
            }
            
            for (int w=0; w<n; w++) {
                String word = words[w];
                if (!visited[w]) {
                    int diff_cnt = 0;
                    for (int i=0; i<word.length(); i++) {
                        if (word.charAt(i) != cmp_char.charAt(i)) { // charAt으로 문자열 인덱스
                            ++diff_cnt;
                        }
                    }
                    if (diff_cnt == 1) {
                        visited[w] = true;
                        q.add(Arrays.asList(word, cmp_cnt+1));
                    }
                }
            }
        }
        
        return answer;
    }
}
