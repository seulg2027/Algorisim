/**
 * prg_42578
 * 아이디어가 중요한 문제
 */
import java.util.HashMap;

public class prg_42578 {

    public int solution(String[][] clothes) {
        HashMap<String, Integer> clothMap = new HashMap<>();

        // 옷의 종류별로 HashMap에 개수를 센다.
        for (String[] cloth : clothes) {
            clothMap.put(cloth[1], clothMap.getOrDefault(cloth[1], 0) + 1);
        }
        
        int answer = 1;
        
        // 각 종류의 옷을 입는 경우의 수를 곱해준다.
        for (int count : clothMap.values()) {
            answer *= (count + 1); // 각 종류별로 안 입는 경우도 고려해서 +1
        }
        
        // 모두 안 입는 경우는 제외한다.
        return answer - 1;
    }
}