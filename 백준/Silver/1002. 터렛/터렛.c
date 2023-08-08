#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<math.h>

int distance(int, int);
int main()
{
	int T,i; //test case
	scanf("%d", &T);
	for (i = 0; i < T; i++)
	{
		int x1, y1, r1; //규현씨 좌표
		int x2, y2, r2; //승환씨 좌표
		int distanceX;
		int distanceY;
		int biggerr;
		int smaller;
		double d; // 실제 좌표 사이 거리
		scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
		if (x1 == x2 && y1 == y2 && r1 == r2)
		{
			printf("-1\n");
			continue;
		}
		distanceX = distance(x1, x2);
		distanceY = distance(y1, y2);
		d = sqrt(distanceX + distanceY);

		biggerr = r1 >= r2 ? r1 : r2;
		smaller = r1 < r2 ? r1 : r2;
		if (d == biggerr + smaller)
			printf("1\n");
		else if (d == biggerr - smaller)
			printf("1\n");
		else if (d > biggerr + smaller)
			printf("0\n");
		else if (d < biggerr - smaller)
			printf("0\n");
		else if (d < biggerr + smaller)
			printf("2\n");
		else if (d > biggerr - smaller)
			printf("2\n");

		
	}
}
int distance(int x1, int x2)
{
	return pow(x1 - x2, 2);
}
