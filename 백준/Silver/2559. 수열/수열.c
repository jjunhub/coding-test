#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    int N, K; // N = 전체 날짜 수, K = 연속적인 날짜 수
    int a, b, maxtemp = 0, t, i;
    int temp[100002] = { 0 };
    int ptr1, ptr2;

    int sum;

    scanf("%d %d", &N, &K);
    for (a = 0; a < N; a++)
    {
        int flag;
        scanf("%d ", &flag);
        temp[a] = flag;
    }

    for (b = 0; b < K; b++)
    {
        maxtemp += temp[b];
    }

    sum = maxtemp;
     
    //printf("sum is %d\n maxtemp is %d\n\n\n\n", sum, maxtemp);
    for (t = 0, i = K; i < N; t++, i++)
    {
        ptr1 = temp[t]; // 맨 앞
        ptr2 = temp[i]; // 맨 뒤 한 칸 뒤

        sum = sum - ptr1;
        sum = sum + ptr2;

       // printf("ptr1 : %d, ptr2 : %d\n", ptr1, ptr2);
       // printf("t is %d, i is %d\n", t, i);
      //  printf("sum is %d\n", sum);

        if (maxtemp <= sum)
            maxtemp = sum;

     //   printf("maxtemp is %d\n\n", maxtemp);


    }
    printf("%d", maxtemp);
    return 0;
}