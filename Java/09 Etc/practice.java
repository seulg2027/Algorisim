
/**
 * java 연습
 */
import java.util.*;
import java.io.*;

public class practice {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 1차원 배열 정렬
        int[] arr = { 89, 18, 20, 71, 31, 63 };

        Integer[] sortedArr = Arrays.stream(arr).boxed().toArray(Integer[]::new);
        Arrays.sort(sortedArr, Collections.reverseOrder());
        System.out.println(Arrays.toString(sortedArr));

        // 2차원 배열 정렬
        int[][] matrix = { { 1, 10 }, { 30, 5 }, { 30, 100 }, { 3, 20 }, { 40, 20 } };

        // 첫번째 원소 기준으로 정렬하기 (오름차순)
        Arrays.sort(matrix, (o1, o2) -> (o1[0] == o2[0] ? o1[1] - o2[1] : o1[0] - o2[0]));
        System.out.println(Arrays.deepToString(matrix));

        // 두번째 원소 기준으로 정렬하기 (내림차순)
        Arrays.sort(matrix, (o1, o2) -> (o1[1] == o2[1] ? o2[0] - o1[0] : o2[1] - o1[1]));
        System.out.println(Arrays.deepToString(matrix));

        /*
         * arrayList 정렬
         */
        ArrayList<Integer> list = new ArrayList<>(Arrays.asList(0, 30, 20, 10));
        Collections.sort(list, Collections.reverseOrder()); // 내림차순 정렬
        System.out.println(list.toString());

        /*
         * map 정렬
         */
        HashMap<Integer, String> map = new HashMap<>();
        map.put(2, "apple");
        map.put(1, "banana");
        List<Integer> keys = new ArrayList<Integer>(map.keySet());
        keys.sort((o1, o2) -> map.get(o2).compareTo(map.get(o1)));
        
        for (Integer key: keys) {
            bw.write(map.get(key) + "\n");
        }

        /*
         * List -> Array 로 변경하기
         */
        int[] intArr = list.stream().mapToInt(i->i).toArray();
        bw.write(Arrays.toString(intArr) +  "\n");

        String[] strArr = list.stream().map(String::valueOf).toArray(String[]::new);
        bw.write(Arrays.toString(strArr) +  "\n");

        list.stream().toArray(Integer[]::new);
        
        /*
         * Array -> List 로 변경하기
         */
        List<int[]> listMatrix = Arrays.asList(matrix);
        Collections.sort(listMatrix, (o1, o2) -> (o1[0] == o2[0] ? o1[1] - o2[1] : o1[0] - o2[0]));
        bw.write("Array -> List : " + Arrays.deepToString(listMatrix.stream().toArray(int[][]::new)) + "\n");
        
        /*
         * Array Generic 형변환
         */
        Arrays.stream(arr).boxed().map(String::valueOf).toArray(String[]::new);

        bw.flush();
        bw.close();
    }
}