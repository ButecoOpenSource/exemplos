#include <stdio.h>
#include <alsa/asoundlib.h>

int main(int argc, char* argv[])
{
	long vol_min = 0, vol_max = 0, vol = 0;
	snd_mixer_t *handle;
	snd_mixer_elem_t *elem;
	snd_mixer_selem_id_t *sid;
	snd_mixer_selem_channel_id_t channel = SND_MIXER_SCHN_FRONT_LEFT;

	snd_mixer_open(&handle, 0);
	snd_mixer_attach(handle, "default");
	snd_mixer_selem_register(handle, NULL, NULL);
	snd_mixer_load(handle);

	snd_mixer_selem_id_alloca(&sid);
	snd_mixer_selem_id_set_index(sid, 0);

	// pegar volume minimo e máximo
	// Master aqui se refere ao volume de saida
	// geralmente esse é o nome da configuração de volume da máquina
	snd_mixer_selem_id_set_name(sid, "Master");
	elem = snd_mixer_find_selem(handle, sid);

	snd_mixer_selem_get_playback_volume_range(elem, &vol_min, &vol_max);

	printf("Volume mínimo: %ld e máximo: %ld\n", vol_min, vol_max);

	if (argc == 1) {
		fprintf(stderr, "Voce precisa passar um valor %ld e %ld como volume\n", vol_min, vol_max);
		return 1;
	}

	snd_mixer_selem_set_playback_volume_all(elem, atol(argv[1]));

	snd_mixer_selem_get_playback_volume(elem, channel, &vol);
	printf("Volume atual: %ld\n", vol);

	return 0;
}
