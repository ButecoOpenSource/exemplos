#include <limits.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include <sys/stat.h>

int main()
{
	struct stat st;
	if (stat("meu_fifo", &st) == -1) {
		printf("Arquivo fifo nao existe. Execute o ./ler para cria-lo\n");
		exit(EXIT_FAILURE);
	}

	int fd = open("meu_fifo", O_WRONLY);
	if (fd == -1) {
		perror("open");
		exit(EXIT_FAILURE);
	}

	while (1) {
		char buf[PIPE_BUF];
		if (fgets(buf, PIPE_BUF, stdin) == NULL) {
			perror("fgets");
			break;
		}
		write(fd, buf, strlen(buf) + 1);
	}

	close(fd);
	exit(EXIT_SUCCESS);
}
