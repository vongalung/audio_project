from audlibs.basic_tones.sinusoidal import *
from player.basicplayer import basicplayer
from sources import notes
class audio(object):
	def __init__(self):
		self._s_rate = None
		self._sample = None
		self._audio = np.array([])
		self._notes = notes.NOTES
		self._notes_per_second = notes.NOTES_PER_SECOND
	def set_sampling(self,rate=44100):
		if not self._s_rate is None:
			raise Exception("Sample Rate has been initialized as %d!" % self._s_rate)
		elif isinstance(rate,int):
			self._s_rate = rate
		else:
			raise Exception("Sample Rate should be of integer type!")
	def set_notes(self,note_set=None,note_second=None):
		if note_set is None:
			None
		elif isinstance(note_set,list):
			self._notes = note_set
		else:
			raise Exception("Notes should be in a list!")
		if note_second is None:
			None
		elif isinstance(note_second,int):
			self._notes_per_second = note_second
		else:
			raise Exception("Notes per Second should be of integer type!")

	def __note(self,name,funct):
		return funct(self._notes[name],self._sample)
	def generate(self,tones,duration=1,funct=SIN):
		try:
			self._sample = np.arange(0,duration/self._notes_per_second,1/self._s_rate)
			aud=np.tile(0,len(self._sample))
			for tone in tones:
				aud=aud+self.__note(tone,funct)
			return aud
		except Exception as e:
			raise e
	def write_audio(self,tones,duration=1,funct=SIN):
		self._audio=np.hstack((self._audio,self.generate(tones,duration,funct)))
	def reset_audio(self,reset_all=False):
		self._audio = np.array([])
		if reset_all:
			self._s_rate = None
			self._sample = None
			self._blank = None

	def normalize(self,audio_buffer):
		norm = (audio_buffer*32767)/np.max(np.abs(audio_buffer))
		return norm.astype(np.int16)
	def run_audio(self,audio_buffer=None,s_rate=None,reset=False):
		basicplayer.play(self.normalize(self._audio if audio_buffer is None else audio_buffer),(self._s_rate if s_rate is None else s_rate))
		if reset:
			reset_audio()
