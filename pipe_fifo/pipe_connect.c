#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main()
{
	int fds[2];

	if (pipe(fds) == -1) {
		perror("pipe");
		return EXIT_FAILURE;
	}

	switch (fork()) {
	case -1:
		perror("fork1");
		return EXIT_FAILURE;
	case 0: // first child: exec ls to write to pipe
		if (close(fds[0]) == -1) {
			perror("close 1");
			return EXIT_FAILURE;
		}

		// Duplicate stdout on write end of pipe and close duplicated descriptor
		if (fds[1] != STDOUT_FILENO) { // defensive check to verify is the write pipe wasn't reset before
			if (dup2(fds[1], STDOUT_FILENO) == -1) {
				perror("dup2 1");
				return EXIT_FAILURE;
			}

			if (close(fds[1]) == -1) {
				perror("close 2");
				return EXIT_FAILURE;
			}
		}

		execlp("ls", "ls", (char *)NULL); // this will write the output of ls command into the write end of pipe
		return EXIT_FAILURE; // SHOULD NOT HIT HERE!
	default: // parent, needs to creat next child
		break;
	}

	switch (fork()) {
	case -1:
		perror("fork2");
		return EXIT_FAILURE;
	case 0: // second child: exec wc to read from pipe
		if (close(fds[1]) == -1) { // close write pipe
			perror("close 3");
			return EXIT_FAILURE;
		}

		// Duplicate stdin on read end of pipe and close duplicated descriptor
		if (fds[0] != STDIN_FILENO) { // defensive check to verify is the read pipe wasn't reset before
			if (dup2(fds[0], STDIN_FILENO) == -1) {
				perror("dup2 2");
				return EXIT_FAILURE;
			}

			if (close(fds[0]) == -1) {
				perror("close 4");
				return EXIT_FAILURE;
			}
		}

		execlp("wc", "wc", "-l", (char *)NULL); // read the pipe, full 
		return EXIT_FAILURE; // SHOULD NOT HIT HERE!
	default: // parent, doest nothing
		break;
	}

	// parent closes all unused fds for pipe and waits for children
	if (close(fds[0]) == -1) {
		perror("close 5");
		return EXIT_FAILURE;
	}
	if (close(fds[1]) == -1) {
		perror("close 6");
		return EXIT_FAILURE;
	}

	if (wait(NULL) == -1) {
		perror("wait 1");
		return EXIT_FAILURE;
	}

	if (wait(NULL) == -1) {
		perror("wait 2");
		return EXIT_FAILURE;
	}

	return EXIT_SUCCESS;
}
