#include <execinfo.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define SIZE 1000

void handler(int sig)
{
	void *buf[SIZE];
	int pts;

	pts = backtrace(buf, SIZE);
	fprintf(stderr, "Signal: %d\n", sig);
	fprintf(stderr, "backtrace returned %d entries\n", pts);

	backtrace_symbols_fd(buf, pts, STDERR_FILENO);
	exit(EXIT_FAILURE);
}

void func2()
{
	int *i = (int *)-1;
	printf("%d", *i); // will trigger SIGSEGV
}

void func1()
{
	// if within 20 seconds the program don't get a SIGINT,
	// it'll trigger a SIGSEGV
	sleep(20);
	func2();
}

int main()
{
	signal(SIGSEGV, handler);
	signal(SIGINT, handler);

	func1();

	return EXIT_SUCCESS; // will never reach, but needed by compiler
}
