/**
 * prg_87946
 * 피로도
 * Java에는 permutations 모듈이 없어 외워야 함
 */
public class prg_87946 {
    static int n, r;
    static int[] output;
    static boolean[] visited;
    static int result;
    static int answer;
    
    public int solution(int k, int[][] dungeons) {
        answer = -1;
        // nPr 순열
        n = dungeons.length;
        r = dungeons.length;
        output = new int[r];
        visited = new boolean[n];
        permutations(0, dungeons, k);
        
        return answer;
    }
    
    // 던전 순서를 거쳐가며 탐험 던전 개수 계산, 최댓값 갱신
    private static void permutations(int cnt, int[][] dungeons, int k) {
        if (cnt == r) {
            result = 0;
            // output -> 던전 순서
            // 던전 순서 차례대로 피로도 차감하면서 계산
            for (int c : output) {
                if (k >= dungeons[c][0]) {
                    k -= dungeons[c][1];
                    result ++;
                } else {
                    break;
                }
            }
            answer = answer >= result ? answer : result; // 최댓값 갱신
            return;
        }
        for (int i=0; i<n; i++) {
            if (visited[i]) continue;
            
            output[cnt] = i;
            visited[i] = true;
            permutations(cnt+1, dungeons, k);
            visited[i] = false;
        }
    }
}