#include <stdio.h>
#include <stdlib.h>

#include <openssl/md5.h>

int main(int argc, char *argv[])
{
	if (argc < 2) {
		fprintf(stderr, "Uso: ./md5_generator <caminho/para/arquivo>. Abortando!\n");
		exit(EXIT_FAILURE);
	}

	FILE *f;
	if ((f = fopen(argv[1], "r")) == NULL) {
		fprintf(stderr, "Arquivo %s não pode ser aberto! ", argv[1]);
		perror("motivo");
		exit(EXIT_FAILURE);
	}

	MD5_CTX mContext;
	MD5_Init(&mContext);

	int bytes;
	unsigned char buf[1024];
	unsigned char digest[MD5_DIGEST_LENGTH];
	char converted[MD5_DIGEST_LENGTH];

	while((bytes = fread(buf, 1, 1024, f)) != 0)
		MD5_Update(&mContext, buf, bytes);

	fclose(f);

	MD5_Final(digest, &mContext);

	// converter o unsigned char para char
	int i;
	for (i = 0; i < MD5_DIGEST_LENGTH; i++)
		sprintf(&converted[i*2], "%02x", digest[i]);

	printf("%s  %s\n", converted, argv[1]);

	exit(EXIT_SUCCESS);
}
