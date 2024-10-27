/**
표의 행
1. U X
2. D X
3. C 삭제 -> 아래 행 선택
4. Z 복구
ArrayList 원소 {0, 1, 2, 3, ..}
연산은 STACK

첫번째 풀이
*/

/**
import java.util.*;

class Solution {
    public String solution(int n, int k, String[] cmd) {
        ArrayList<Integer> list = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();
        
        for (var i=0; i<n; i++) {
            list.add(i);
        }
        
        for (String c : cmd) {
            String[] item = c.split(" ");
            if (item[0].equals("U")) {
                k -= Integer.parseInt(item[1]);
            } else if (item[0].equals("D")) {
                k += Integer.parseInt(item[1]);
            } else if (item[0].equals("C")) {
                stack.add(list.get(k));
                list.remove(k);
                if (k >= list.size()) {
                    k -= 1;
                }
            } else if (item[0].equals("Z")) {
                int a = stack.pop();
                if (a < list.get(k)) {
                    k += 1;
                }
                list.add(a);
            }
            Collections.sort(list);
        }
        
        StringBuilder sb = new StringBuilder();
        
        for (var i=0; i<n; i++) {
            if (list.contains(i)) sb.append("O");
            else sb.append("X");
        }
        
        return sb.toString();
    }
}
**/

import java.util.*;

class Solution {
    public String solution(int n, int k, String[] cmd) {
        int[] pre = new int[n];
        int[] next = new int[n];
        for(int i = 0; i < n; i++) {
            pre[i] = i - 1;
            next[i] = i + 1;
        }
        next[n - 1] = -1;
        
        Stack<Node> stack = new Stack<>();
        StringBuilder sb = new StringBuilder("O".repeat(n));
        
        for(int i = 0; i < cmd.length; i++) {
            char c = cmd[i].charAt(0);
            if(c == 'U') {
                String value = cmd[i].substring(2);
                int num = Integer.valueOf(value);
                while(num-- > 0) {
                    k = pre[k];
                }
            } else if(c == 'D') {
                String value = cmd[i].substring(2);
                int num = Integer.valueOf(value);
                while(num-- > 0) {
                    k = next[k];
                }
            } else if(c == 'C') {
                stack.push(new Node(pre[k], k, next[k]));
                
                if (pre[k] != -1) next[pre[k]] = next[k]; //현재 노드 삭제 후 앞뒤 연결
                if (next[k] != -1) {
                    pre[next[k]] = pre[k];
                }
                
                sb.setCharAt(k, 'X');
                
                if (next[k] != -1) k = next[k];
                else k = pre[k];
            } else {
                Node node = stack.pop();
                
                //연결 정보 복구
                if (node.pre != -1) {
                    next[node.pre] = node.cur;
                }
                if (node.nxt != -1) {
                    pre[node.nxt] = node.cur;
                }
                
                sb.setCharAt(node.cur, 'O');
            }
            
            // System.out.println(Arrays.toString(pre));
            // System.out.println(Arrays.toString(next));
        }
        
        return sb.toString();
    }
    
    private class Node{
        int pre, cur, nxt;
        
        public Node(int pre, int cur, int nxt) {
            this.pre = pre;
            this.cur = cur;
            this.nxt = nxt;
        }
    }
}