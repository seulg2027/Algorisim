/**
 * 11652번 카드
 * 개수가 많은 카드대로
 */
import java.io.*;
import java.util.*;

public class boj_카드 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        HashMap<Long, Integer> numberCard = new HashMap<>();

        for (int i=0; i<N; i++) {
            long card = Long.parseLong(br.readLine());
            numberCard.put(card, numberCard.getOrDefault(card, 0) + 1);
        }

        // card 정렬
        List<Long> cardKeys = new ArrayList<>(numberCard.keySet());
        cardKeys.sort((o1, o2) -> numberCard.get(o2).compareTo(numberCard.get(o1))); // 내림차순

        long minKey = cardKeys.get(0);
        int maxValue = numberCard.get(cardKeys.get(0));

        for (int k=1; k<cardKeys.size(); k++) {
            if (maxValue == numberCard.get(cardKeys.get(k))) {
                minKey = Math.min(minKey, cardKeys.get(k));
            } else {
                break;
            }
        }

        bw.write(String.valueOf(minKey) + "\n");

        bw.flush();
        bw.close();
    }
}
