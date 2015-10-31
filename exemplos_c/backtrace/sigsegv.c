#include <stdio.h>

int main()
{
	int x = 1, *y;

	y = (int *)-1;

	printf("%d\n", x);
	printf("%d\n", *y); // SIGSEGV

	return 1;
}
