#include <sys/types.h>
#include <regex.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static void exec_regex(char *str, char *pat, int args)
{
	regex_t reg;
	printf("String '%s', Pattern '%s'\n", str, pat);

	if (regcomp(&reg, pat, args)) {
		fprintf(stderr, "Could not compiled regex\n");
		return;
	}

	int ret, nsub = reg.re_nsub;
	// if nsub == 0 | > 1, add 1 to show the one string matches
	if (nsub != 1)
		nsub++;

	regmatch_t matchptr[nsub];

	if ((ret = regexec(&reg, str, nsub, matchptr, 0))) {
		if (ret == REG_NOMATCH) {
			fprintf(stderr, "\tREG_NOMATCH\n");
		} else {
			char err[100];
			regerror(ret, &reg, err, sizeof(err));
			fprintf(stderr, "\tRegex failed: %s\n", err);
		}
		return;
	} else {
		int i;

		for (i = 0; i < nsub; i++) {
			if (matchptr[i].rm_so == -1)
				break;

			// create a string long enough to store the original str, and set init and end offset
			char string[strlen(str) + 1];
			char *start = str + matchptr[i].rm_so;
			size_t end = matchptr[i].rm_eo - matchptr[i].rm_so;

			// copy the the string by the offsets and set the NULL byte
			strncpy(string, start, end);
			string[end] = '\0';
			printf("\tGroup %d: [%u-%u]: %s\n", i, matchptr[i].rm_so, matchptr[i].rm_eo, string);
		}
	}

	regfree(&reg);
	return;
}

static void exec_regex_basic(char *str, char *pat)
{
	exec_regex(str, pat, 0);
}

static void exec_regex_extended(char *str, char *pat)
{
	exec_regex(str, pat, REG_EXTENDED);
}

int main()
{
	printf("Executing basic Regex\n");
	exec_regex_basic("buteco123xxxxx", "\\([a-z]*\\)");
	exec_regex_basic("buteco123xxxxx", "\\([a-z]+\\)\\([0-9]+\\)");
	exec_regex_basic("buteco123xxxxx", "\\([a-z]*\\)\\([0-9]*\\)");
	exec_regex_basic("buteco123xxxxx", "\\([[:alpha:]]*\\)");

	printf("\nExecuting extended Regex\n");
	exec_regex_extended("buteco123xxxxx", "([a-z]*)");
	exec_regex_extended("buteco123xxxxx", "([a-z]+)([0-9]+)");
	exec_regex_extended("buteco123xxxxx", "([a-z]*)([0-9]*)");
	exec_regex_extended("buteco123xxxxx", "([[:alpha:]]*)");
	exec_regex_extended("buteco123xxxxx", "([^[:space:]]+)");
	exec_regex_extended("buteco123xxxxx", "([[:digit:]]+)");
	exec_regex_extended("buteco123xxxxx", "([[:upper:]]+)");
	exec_regex_extended("buteco123xxxxx", "([[:lower:]])");

	exit(EXIT_SUCCESS);
}
