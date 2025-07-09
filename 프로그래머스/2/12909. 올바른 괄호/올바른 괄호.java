/**
*  닫힌 괄호가 들어왔을 때, 열린 괄호가 남아있어야한다.
*  ( 가 들어오면, +1을 진행해주고,
*  ) 가 들어오면, -1을 해줍니다.
*  값이 음수로 되는 순간이 있다면 실패.
**/
class Solution {
    public static char OPEN = '(';
    // public static String CLOSE = ")";
    
    boolean solution(String s) {
        boolean answer = true;
        Integer numberOfOpen = 0;
        
        for( char c : s.toCharArray()) {
            if (c == OPEN) {
                numberOfOpen += 1;
            } else {
                numberOfOpen -=1;
            }
            
            if (numberOfOpen < 0) {
                answer = false;
            }
        }
        
        if (numberOfOpen != 0) {
            answer = false;
        }
    
        return answer;
    }
}