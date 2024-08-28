import java.util.*;

public class prg_성격유형검사하기 {
    // 첫번째 시도
    class Solution {
        public String solution(String[] survey, int[] choices) {
            StringBuilder answer = new StringBuilder("");
            int[][] result = new int[4][2];
            String[][] personality = {{"R", "T"}, {"C", "F"}, {"J", "M"}, {"A", "N"}};
            
            for (int i = 0; i < survey.length; i++) {
                int intChoice = 0;
                String select = survey[i];
                if (select.startsWith("R") || select.startsWith("T")) {
                    intChoice = 0;
                } else if (select.startsWith("C") || select.startsWith("F")) {
                    intChoice = 1;
                } else if (select.startsWith("J") || select.startsWith("M")) {
                    intChoice = 2;
                } else if (select.startsWith("A") || select.startsWith("N")) {
                    intChoice = 3;
                }
                char c = select.charAt(0);
                
                if (c == 'R' || c == 'C' || c == 'J' || c == 'A'){
                    if (choices[i] >= 4) {
                        result[intChoice][1] += Math.abs(choices[i]-4);
                    } else {
                        result[intChoice][0] += Math.abs(choices[i]-4);
                    }
                } else {
                    if (choices[i] >= 4) {
                        result[intChoice][0] += Math.abs(choices[i]-4);
                    } else {
                        result[intChoice][1] += Math.abs(choices[i]-4);
                    }
                }
            }
            //System.out.println(Arrays.deepToString(result));
            for (int i = 0; i < 4; i++) {
                if (result[i][0] >= result[i][1]) answer.append(personality[i][0]);
                else answer.append(personality[i][1]);
            }
            //System.out.println(answer);
            String strAns = answer.toString();
            
            return strAns;
        }
    }

    // 두번째 시도
    class Solution {
        public String solution(String[] survey, int[] choices) {
            String answer = "";
            HashMap<String, Integer> personality = new HashMap<>();
            
            for (int i=0; i<survey.length; i++) {
                if (choices[i] < 4) {
                    String s = String.valueOf(survey[i].charAt(0));
                    personality.put(s, personality.getOrDefault(s, 0) + 4 - choices[i]);
                } else if (choices[i] > 4){
                    String s = String.valueOf(survey[i].charAt(1));
                    personality.put(s, personality.getOrDefault(s, 0) + choices[i] - 4);
                }
            }
            
            StringBuilder sb = new StringBuilder();
            
            sb.append(personality.getOrDefault("R", 0) >= personality.getOrDefault("T", 0) ? "R" : "T")
              .append(personality.getOrDefault("C", 0) >= personality.getOrDefault("F", 0) ? "C" : "F")
              .append(personality.getOrDefault("J", 0) >= personality.getOrDefault("M", 0) ? "J" : "M")
              .append(personality.getOrDefault("A", 0) >= personality.getOrDefault("N", 0) ? "A" : "N");
            
            answer = sb.toString();
            
            return answer;
        }
    }
}
