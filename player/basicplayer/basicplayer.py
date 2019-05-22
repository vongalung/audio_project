import simpleaudio as sa

def play(audio_buffer,s_rate):
	try:
		play_obj = sa.play_buffer(audio_buffer,2,2,s_rate)
		play_obj.wait_done()
	except Exception as e:
		raise e

def cont_play(audio_buffer,s_rate):
	try:
		play_obj = sa.play_buffer(audio_buffer,2,2,s_rate)
	except Exception as e:
		raise e
