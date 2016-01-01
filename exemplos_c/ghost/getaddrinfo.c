#include <stdio.h>
#include <stdlib.h>

#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>

#include <arpa/inet.h>

int main(int argc, char **argv)
{
	if (argc < 2) {
		fprintf(stderr, "Usage: getaddrinfo <host or IP>\n");
		exit(EXIT_FAILURE);
	}

	int ret;
	struct addrinfo *res, *p, hints;

	hints.ai_family = AF_UNSPEC;
	hints.ai_socktype = 0;
	hints.ai_flags = AI_CANONNAME;

	if ((ret = getaddrinfo(argv[1], NULL, &hints, &res))) {
		fprintf(stderr, "Error getaddrinfo: %s\n", gai_strerror(ret));
		exit(EXIT_FAILURE);
	}

	printf("Host: %s\n", res->ai_canonname);

	char addr[INET6_ADDRSTRLEN];
	for (p = res; p != NULL; p = p->ai_next) {
		void *ptr = NULL;
		if (p->ai_family == AF_INET) {
			struct sockaddr_in *in = (struct sockaddr_in *)p->ai_addr;
			ptr = &(in->sin_addr);
			printf("IPv4: ");
		} else if (p->ai_family == AF_INET6) {
			struct sockaddr_in6 *in6 = (struct sockaddr_in6 *)p->ai_addr;
			ptr = &(in6->sin6_addr);
			printf("IPv6: ");
		}

		if (!inet_ntop(p->ai_family, ptr, addr, INET6_ADDRSTRLEN)) {
			perror("inet_ntop");
			exit(EXIT_FAILURE);
		}
		printf("%s\n", addr);
	}

	freeaddrinfo(res);
	exit(EXIT_SUCCESS);
}
