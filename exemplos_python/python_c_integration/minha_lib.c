#include <stdio.h>

int soma(int n, int m)
{
	return n + m;
}

int inc(int n)
{
	return ++n;
}

void cria_arquivo(char* fname)
{
	FILE* f = fopen(fname, "w");
	if (!f) {
		perror("fopen");
		return;
	}

	fprintf(f, "Arquivo criado pela lib");
	fclose(f);
}
