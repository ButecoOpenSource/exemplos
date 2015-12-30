#include <netdb.h>
#include <stdlib.h>
#include <stdio.h>

#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main(int argc, char **argv)
{
	if (argc < 2) {
		printf("Usage: gethostbyname <address or hostname>\n");
		return EXIT_FAILURE;
	}

	struct hostent *ht = gethostbyname(argv[1]);
	if (!ht) {
		printf("Error: %s\n", hstrerror(h_errno));
		return EXIT_FAILURE;
	}

	printf("Host: %s\n", ht->h_name);

	int i;
	if (ht->h_addrtype == AF_INET) {
		for (i = 0; ht->h_addr_list[i] != NULL; i++) {
			struct in_addr *tmp = (struct in_addr *)ht->h_addr_list[i];
			printf("IP: %s\n", inet_ntoa(*tmp));
		}
	} else { // AF_INET6
		//struct in6_addr *tmp = (struct in6_addr *)ht->h_addr_list[i];
		printf("IPv6 TODO\n");
	}
	return EXIT_SUCCESS;
}
