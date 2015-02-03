#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void meChama()
{
	printf("Chamado no encerramento do programa\n");
}

int main(int argc, char *argv[])
{
	// registrar a função que irá ser chamada ao encerrar o processo
	atexit(meChama);

	printf("A função meChama irá ser chamada no encerramento "
			"do processo\n");
	sleep(3);

	exit(EXIT_SUCCESS);
}
