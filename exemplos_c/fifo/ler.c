#include <limits.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main()
{
	struct stat st;
	// criar fifo se nao existir
	if (stat("meu_fifo", &st) == -1) {
		if (mkfifo("meu_fifo", 0666) == -1) {
			perror("mkfifo");
			exit(EXIT_FAILURE);
		}
		printf("fifo criado\n");
	} else {
		printf("fifo meu_fifo previamente criado\n");
	}

	int fd = open("meu_fifo", O_RDONLY);
	if (fd == -1) {
		perror("open");
		exit(EXIT_FAILURE);
	}

	char buf[PIPE_BUF];
	while (1) {
		if (read(fd, &buf, PIPE_BUF) == 0) {
			printf("Fifo fechado na outra ponta\n");
			break;
		}
		printf("Lido: %s", buf);
	}

	close(fd);

	exit(EXIT_SUCCESS);
}
