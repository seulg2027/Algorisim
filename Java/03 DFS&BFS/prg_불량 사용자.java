/**
* 
중복없는 순열
["frodo", "crodo", "abc123", "frodoc"]
*/
import java.util.*;

class Solution {
    HashSet<String> set;
    boolean[] visited;
    
    public int solution(String[] user_id, String[] banned_id) {
        int n = banned_id.length;
        set = new HashSet<>();
        visited = new boolean[user_id.length];
        
        for (int i=0; i<n; i++) {
            banned_id[i] = banned_id[i].replace("*", ".");
        }
        permutations(0, user_id, banned_id, new String[n]);
        
        return set.size();
    }
    
    private void permutations(int cnt, String[] user_id, String[] banned_id, String[] alert_id) {
        if (cnt == banned_id.length) {
            String[] arr = Arrays.copyOf(alert_id, alert_id.length);
            Arrays.sort(arr);
            String str = String.join("", arr);
            //System.out.println(str);
            set.add(str);
            return;
        }
        
        for (int i=0; i<user_id.length; i++) {
            if (visited[i] || !user_id[i].matches(banned_id[cnt])) continue;
            
            visited[i] = true;
            alert_id[cnt] = user_id[i];
            permutations(cnt+1, user_id, banned_id, alert_id);
            visited[i] = false;
        }
    }
}