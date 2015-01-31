#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	// fd 0 read side
	// fd 1 write side
	int fds[2];
	char buf[255];

	if (pipe(fds) == -1) {
		perror("pipe");
		return EXIT_FAILURE;
	}

	// at this point, a new process will be created and will execute the same as father
	// the only thing that can jail each process is to test the return of fork system call.
	// The fork syscall returns 0 in the new process, while return the pid of parent in the case
	// of the parent process
	switch(fork()) {
	case -1:
		perror("fork");
		return EXIT_FAILURE;
	case 0: // child process
		if (close(fds[1]) == -1) // closes the write fd as it will not be used
			perror("Child close");

		// child process will wait to read message of parent process
		if (read(fds[0], buf, sizeof(buf)) == -1) {
			perror("Child read");
			return EXIT_FAILURE;
		}

		printf("Child readed: %s\n", buf);
		break;

	default: // parent
		if (close(fds[0]) == -1) // closes the read fd as it will not be used
			perror("Child close");

		// parent process writea message to child process
		strncpy(buf, "Hello from parent! Have a long life!", sizeof(buf));
		if (write(fds[1], buf, sizeof(buf)) == -1) {
			perror("Parent write");
			return EXIT_FAILURE;
		}

		printf("Parent wrote the message!\n");
		break;
	}

	return EXIT_SUCCESS;
}
