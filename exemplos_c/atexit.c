#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void meChama()
{
	printf("Chamado no encerramento do programa\n");
}

void meChama2()
{
	printf("Serei chamado primeiro!!\n");
}

int main(int argc, char *argv[])
{
	// registrar a função que irá ser chamada ao encerrar o processo
	atexit(meChama);
	atexit(meChama2);

	printf("As funções serão chamadas no encerramento "
			"do processo\n");
	sleep(3);

	exit(EXIT_SUCCESS);
}
