#include <stdio.h> // perror

#include <sys/ioctl.h> // funcao ioctl
#include <linux/cdrom.h> // CDROM*

// necessarios para a chamada open
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#include <unistd.h> // funcao close
#include <stdlib.h> // EXIT_SUCCESS, EXIT_FAILURE

int main()
{
	// aqui o /dev/cdrom é um link para /dev/sr0, mas ambos funcionam
	int fd = open("/dev/cdrom", O_RDONLY | O_NONBLOCK);
	if (fd == -1) {
		perror("open");
		return EXIT_FAILURE;
	}

	// slot sempre 0, a nao ser para jukeboxes
	int state = ioctl(fd, CDROM_DRIVE_STATUS, 0);
	if (state < 0) {
		perror("ioctl state");
		return EXIT_FAILURE;
	}

	int aberto = 0;
	int error = 0;

	switch(state) {
	// Sem informacao disponivel
	case (CDS_NO_INFO):
	// Drive nao esta pronto
	case (CDS_DRIVE_NOT_READY):
		error = 1;
		break;
	// Bandeja aberta
	case (CDS_TRAY_OPEN):
		aberto = 1;
		break;
	// Sem disco
	case (CDS_NO_DISC):
	// Disco OK
	case (CDS_DISC_OK):
		break;
	}

	if (error) {
		printf("Erro ao verificar estado do CDROM. Abortando\n");
		return EXIT_FAILURE;
	}

	if (!aberto) {
		printf("Destravando bandeja\n");
		// 0 - unlock
		// 1 - lock
		if (ioctl(fd, CDROM_LOCKDOOR, 0) < 0) {
			perror("ioctl unlock");
			return EXIT_FAILURE;
		}

		printf("Abrindo bandeja do CDROM\n");
		if (ioctl(fd, CDROMEJECT, 0) < 0) {
			perror("ioctl open");
			return EXIT_FAILURE;
		}
		printf("Aguarda 5 segundos para fechar a bandeja do CDROM novamente\n");
		sleep(5);
	}

	printf("Fechando bandeja\n");

	if (ioctl(fd, CDROMCLOSETRAY, 0) < 0) {
		perror("ioctl close");
		return EXIT_FAILURE;
	}

	if (close(fd) == -1) {
		perror("close");
		return EXIT_FAILURE;
	}

	return EXIT_SUCCESS;
}
