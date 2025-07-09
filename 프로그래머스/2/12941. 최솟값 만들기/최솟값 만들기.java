import java.util.*;

class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;
        Arrays.sort(A);
        Arrays.sort(B);

        Integer len = A.length;

        for (int idx = 0; idx < A.length; idx++) {
          answer += A[idx] * B[len-1-idx];
        }

        return answer;
    }
}