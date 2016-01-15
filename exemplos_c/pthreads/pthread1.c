#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

#include <pthread.h>

void *func(void *data)
{
	int i, ret = 0, num = *(int *)data;

	for (i = 0; i < 100; i++)
		ret += num;
	return (void *)(intptr_t)ret;
}

int main()
{
	pthread_t t[2];
	int val1 = 5, val2 = 6;
	void *ret = NULL;
	int r1, r2;

	if (pthread_create(&t[0], NULL, func, (void *)&val1)) {
		perror("pthread_create1");
		exit(EXIT_FAILURE);
	}

	if (pthread_create(&t[1], NULL, func, (void *)&val2)) {
		perror("pthread_create2");
		exit(EXIT_FAILURE);
	}

	if (pthread_join(t[0], &ret)) {
		perror("pthread_join");
		exit(EXIT_FAILURE);
	}
	r1 = (intptr_t)ret;

	if (pthread_join(t[1], &ret)) {
		perror("pthread_join2");
		exit(EXIT_FAILURE);
	}
	r2 = (intptr_t)ret;

	printf("Resultado: %d\n", r1 + r2);
	exit(EXIT_SUCCESS);
}
