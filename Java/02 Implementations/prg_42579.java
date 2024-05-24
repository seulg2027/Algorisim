import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

/**
 * prg_42579
 * 베스트앨범
 */
public class prg_42579 {

    public int[] solution(String[] genres, int[] plays) {
        // 장르별 재생 횟수 저장
        HashMap<String, Integer> genresPlays = new HashMap<String, Integer>();
        // 장르별 고유번호, 재생 횟수 저장
        HashMap<String, List<int[]>> genresMap = new HashMap<>();
        
        for (int i=0; i<genres.length; i++) {
            // 장르별 총합 재생횟수
            genresPlays.put(genres[i], genresPlays.getOrDefault(genres[i], 0) + plays[i]);

            // 장르별 (고유번호, 재생횟수) HashMap 생성하기
            int[] now = {i, plays[i]};
            if (!genresMap.containsKey(genres[i])) {
                List<int[]> p = new ArrayList<int[]>();
                p.add(now);
                genresMap.put(genres[i], p);
            } else {
                List<int[]> item = genresMap.get(genres[i]);
                item.add(now);
                genresMap.put(genres[i], item);
            }
        }
        List<String> keys = new ArrayList<>(genresPlays.keySet()); // genresSet
        
        // 내림차순으로 정렬
        keys.sort((o1, o2) -> genresPlays.get(o2).compareTo(genresPlays.get(o1)));
        
        ArrayList<Integer> album = new ArrayList<>();
        
        // keys를 기준으로 순회
        for (int i=0; i<keys.size(); i++) {
            int cnt = 0;
            List<int[]> values = genresMap.get(keys.get(i));
            int arr[][] = values.stream().toArray(int[][]::new);
            // 재생 횟수별로 정렬, 이후 고유번호 순으로 정렬
            Arrays.sort(arr, (o1, o2) -> (o1[1] == o2[1] ? o1[0] - o2[0] : o2[1] - o1[1]));
            
            for (int j=0; j<values.size(); j++) {
                if (cnt == 2) break;
                
                album.add(arr[j][0]);
                cnt ++;
            }
        }
        
        return album.stream().mapToInt(i->i).toArray();
    }
}