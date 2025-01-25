/**
* 네오가 찾으려는 음악의 제목 구하기
1분에 1개씩 재생, 처음부터 재생
음악 길이 < 재생 시간 : 처음부터 반복해서 재생

ABC# => ABC 는 안되도록..
*/
public class prg_방금그곡 {
    class Solution {
        public String solution(String m, String[] musicinfos) {
            String answer = "(None)";
            int longTime = 0;
            
            m = convertMelody(m);
            
            for (var i=0; i<musicinfos.length; i++) {
                String[] info = musicinfos[i].split(",");
                String[] start = info[0].split(":");
                String[] end = info[1].split(":");
                
                // 재생 시간 계산
                int startMinutes = Integer.parseInt(start[0]) * 60 + Integer.parseInt(start[1]);
                int endMinutes = Integer.parseInt(end[0]) * 60 + Integer.parseInt(end[1]);
                int runTime = endMinutes - startMinutes;
                
                String melodyInfo = convertMelody(info[3]);
                StringBuilder sb = new StringBuilder();
                
                for (int k=0; k<runTime; k++) {
                    sb.append(String.valueOf(melodyInfo.charAt(k % melodyInfo.length())));
                }
                
                if (sb.toString().contains(m)) {
                    if (answer.equals("(None)") || longTime < runTime) {
                        answer = info[2];
                        longTime = runTime;
                    }
                }
            }
            
            return answer;
        }
        
        private String convertMelody(String melody) {
            return melody.replaceAll("A#", "a")
                        .replaceAll("B#", "b")
                        .replaceAll("C#", "c")
                        .replaceAll("D#", "d")
                        .replaceAll("F#", "f")
                        .replaceAll("G#", "g");
        }
    }
}