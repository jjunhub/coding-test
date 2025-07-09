/**
*  닫힌 괄호가 들어왔을 때, 열린 괄호가 남아있어야한다.
*  ( 가 들어오면, +1을 진행해주고,
*  ) 가 들어오면, -1을 해줍니다.
*  값이 음수로 되는 순간이 있다면 실패.
**/
class Solution {
    public static char OPEN = '(';
    public static Integer numberOfOpen = 0;
    public static boolean answer = true;
    
    public boolean solution(String s) {

        for (char c : s.toCharArray()) {
            numberOfOpen += decideChar(c);
            checkCloseExceedOpen();
        }
        
        checkRemainGalho();
        return answer;
    }
    
    private static void checkCloseExceedOpen() {
        if (numberOfOpen < 0) {
            answer = false;
        }
    }
    
    private static Integer decideChar(char c) {
        if (c == OPEN) {
            return 1;
        } else {
            return -1;
        }
    }
    
    private static void checkRemainGalho() {
        if (numberOfOpen != 0) {
            answer = false;
        }
    }
}