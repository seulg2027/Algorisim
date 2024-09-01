import java.util.*;

class Solution {
    HashMap<Long, Long> nextHotelMap = new HashMap<>();
    
    public long[] solution(long k, long[] room_number) {
        ArrayList<Long> answer = new ArrayList<>();
        
        // k <= 10**12
        for (long num : room_number) {
            long result = getRoomSearch(num);
            answer.add(result);
        }
        
        return answer.stream().mapToLong(i->i).toArray();
    }
    
    private long getRoomSearch(long x) {
        if (nextHotelMap.getOrDefault(x, (long)0) == 0) {
            nextHotelMap.put(x, x+1);
            return x;
        }
        
        long nextRoom = getRoomSearch(nextHotelMap.get(x));
        nextHotelMap.put(x, nextRoom);
        return nextRoom;
    }
}