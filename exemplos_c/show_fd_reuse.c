#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
	int fd = open("teste.txt", O_CREAT);
	if (!fd) {
		perror("open1");
		exit(EXIT_FAILURE);
	}

	printf("fd aberto é: %d\n", fd);

	if (close(fd) == -1) {
		perror("close1");
		exit(EXIT_FAILURE);
	}

	int fd2 = open("outro_text.txt", O_CREAT);
	if (!fd) {
		perror("open2");
		exit(EXIT_FAILURE);
	}

	printf("novo fd é: %d\n", fd2);

	if (close(fd) == -1) {
		perror("close2");
		exit(EXIT_FAILURE);
	}

	exit(EXIT_SUCCESS);
}
