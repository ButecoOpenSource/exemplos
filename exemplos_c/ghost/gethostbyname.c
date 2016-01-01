#include <netdb.h>
#include <stdlib.h>
#include <stdio.h>

#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

void print_ips(char *hostname, int iptype)
{
	struct hostent *ht = gethostbyname2(hostname, iptype);
	if (!ht) {
		printf("Error: %s\n", hstrerror(h_errno));
		exit(EXIT_FAILURE);
	}

	printf("Host: %s\n", ht->h_name);

	int i;
	char addr[INET6_ADDRSTRLEN];
	for (i = 0; ht->h_addr_list[i] != NULL; i++) {
		void *ptr = NULL;

		if (ht->h_addrtype == AF_INET) {
			struct in_addr *tmp = (struct in_addr *)ht->h_addr_list[i];
			ptr = tmp;
			printf("IPv4: ");
		} else if (ht->h_addrtype == AF_INET6) {
			struct in6_addr *tmp = (struct in6_addr *)ht->h_addr_list[i];
			ptr = tmp;
			printf("IPv6: ");
		}

		if (!inet_ntop(ht->h_addrtype, ptr, addr, INET6_ADDRSTRLEN)) {
			perror("inet_ntop");
			exit(EXIT_FAILURE);
		}

		printf("%s\n", addr);
	}
}

int main(int argc, char **argv)
{
	if (argc < 2) {
		printf("Usage: gethostbyname <address or hostname>\n");
		exit(EXIT_FAILURE);
	}

	print_ips(argv[1], AF_INET);
	print_ips(argv[1], AF_INET6);

	exit(EXIT_SUCCESS);
}
