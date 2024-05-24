/**
 * prg_12909
 */
import java.util.*;

public class prg_12909 {

    boolean solution(String s) {
        boolean answer = true;
        Stack<String> stack = new Stack<>();
        
        // "(" 를 갖는 경우에만 스택에 넣고,
        // 스택에 "(" 이 있으면 ")"와 만날 시 stack에서 pop
        for (int i=0; i<s.length(); i++) {
            if (s.substring(i, i+1).equals("(")) {
                stack.push("(");
            } else {
                if (stack.isEmpty()) {
                    answer = false;
                    break;
                } else {
                    stack.pop();
                }
            }
        }
        
        if (!stack.isEmpty()) {
            answer = false;
        }
        
        return answer;
    }
}