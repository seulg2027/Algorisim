/**
 * boj_11723
 * 집합
 * 비트마스킹인데 파이썬처럼 그냥 풀었다가 예시코드 보고 기겁했다.
 * 자바 개발자인데ㅠㅠ 맞아..? 지금부터라도 익혀두자.
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class boj_11723 {
    static int m;
    static HashSet<Integer> S = new HashSet<>();

    public static void main(String[] args) throws IOException{
        String cal = "";
        int x = 0;
        StringBuilder sb = new StringBuilder();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());

        for (int i=0; i<m; i++) {
            StringTokenizer order = new StringTokenizer(br.readLine());
            cal = order.nextToken();
            
            if (cal.equals("all")) {
                Integer[] arr = new Integer[20];
                Arrays.setAll(arr, j -> j + 1);
                S = new HashSet<>(Arrays.asList(arr));
            } else if (cal.equals("empty")) {
                S.clear();
            } else {
                x = Integer.parseInt(order.nextToken());

                if (cal.equals("add") && !S.contains(x)) addCal(x);
                else if (cal.equals("remove") && S.contains(x)) removeCal(x);
                else if (cal.equals("check") && S.contains(x)) sb.append(1).append("\n");
                else if (cal.equals("check") && !S.contains(x)) sb.append(0).append("\n");
                else if (cal.equals("toggle") && S.contains(x)) removeCal(x);
                else if (cal.equals("toggle") && !S.contains(x)) addCal(x);
            } 
        }

        System.out.println(sb);
    }

    private static void addCal(int x) {
        S.add(x);
    }

    private static void removeCal(int x) {
        S.remove(x);
    }


    // 비트마스크를 활용해 만든 다른 사람의 코드
    public static void example() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int S = 0;
        int M = Integer.parseInt(br.readLine());
        StringTokenizer st;

        // M-- 을 연산했을 때 0보다 크면
        while (M-- > 0) {
            st = new StringTokenizer(br.readLine());
            String str = st.nextToken();
            if(str.equals("all")) S = (1 << 21) - 1;
            else if(str.equals("empty")) S = 0;
            else {
                int num = Integer.parseInt(st.nextToken());
                if(str.equals("add"))
                    S |= (1 << num);
                else if(str.equals("remove"))
                    S &= ~(1 << num);
                else if(str.equals("check"))
                    sb.append((S & (1 << num)) != 0 ? 1 : 0).append("\n");
                else if(str.equals("toggle"))
                    S ^= (1 << num);
            }
        }
        System.out.println(sb);
    }
}
