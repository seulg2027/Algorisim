/**
1. 이모티콘 플러스 가입자 수 늘리기
2. 이모티콘 판매액 늘리기
[40, 10000], [25, 10000] -> 10, 20, 30, 40 할인 가능
40, 40
30, 40
...
4**7 = 16,384
*/
import java.util.Arrays;

public class prg_이모티콘_할인행사 {
    class Solution {
        int n, m;
        int ansCnt = 0, ansPrice = 0;
        int[] perArr;
        int[][] userArr;
        int[] emoArr;
        int[] percents = {40, 30, 20, 10};
        
        public int[] solution(int[][] users, int[] emoticons) {
            n = users.length;
            m = emoticons.length;
            
            perArr = new int[m];
            userArr = users.clone();
            emoArr = emoticons.clone();
            
            Arrays.sort(emoArr);
            Arrays.sort(userArr, (o1, o2) -> o2[0] - o1[0]);
            
            for (int p = 1; p < 4; p++) {
                // 한 명이라도 구매 가능한 할인율부터 중복순열 시작
                if (percents[p] < userArr[0][0]) {
                    getEmoDiscount(m - 1, p - 1);
                }
            }
            
            return new int[]{ansCnt, ansPrice};
        }
        
        private void getEmoDiscount(int cnt, int start) {
            if (cnt == -1) {
                int plus = 0, totalPrice = 0;
                for (int j = 0; j < n; j++) { // 사용자 당 구매한 이모티콘
                    int price = 0;
                    for (int e = 0; e < m; e++) {
                        if (userArr[j][0] <= perArr[e]) {
                            price += (emoArr[e] * (100 - perArr[e]) / 100);
                        }
                    }
                    // 이모티콘 플러스 서비스에 가입했다면 플러스 서비스 추가, 아니면 이모티콘 판매액에 추가
                    if (price >= userArr[j][1]) {
                        plus++;
                    } else {
                        totalPrice += price;
                    }
                }
                
                if (plus > ansCnt) {
                    ansCnt = plus;
                    ansPrice = totalPrice;
                } else if (plus == ansCnt) {
                    ansPrice = Math.max(ansPrice, totalPrice);
                }
                
                return;
            }
            
            for (int i = start; i < 4; i++) {
                perArr[cnt] = percents[i];
                getEmoDiscount(cnt - 1, start);
            }
        }
    }
}
