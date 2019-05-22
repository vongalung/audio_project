from audlibs.basic_tones.sinusoidal import *
from player.basicplayer import basicplayer
from sources import notes
class audio(object):
	def __init__(self):
		self._s_rate = None
		self._sample = None
		self._audio = np.array([])
		self._blank = None
	def set_sampling(self,rate=44100):
		if not self._sample is None:
			raise Exception("Sample Rate has been initialized as %d!" % self._sample)
		elif isinstance(rate,int):
			self._s_rate = rate
			self._sample = np.arange(0,1,1/self._s_rate)
			self._blank = np.tile(0,self._s_rate)
		else:
			raise Exception("Sample Rate should be of integer type!")

	def __note(self,name,duration,funct):
		return np.tile(funct(notes.NOTES[name],self._sample),duration)
	def generate(self,tones,duration=1,funct=SIN):
		try:
			aud=np.tile(self._blank,duration)
			for tone in tones:
				aud=aud+self.__note(tone,duration,funct)
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
	def run_audio(self,audio_buffer=None,s_rate=None):
		basicplayer.play(self.normalize(self._audio if audio_buffer is None else audio_buffer),(self._s_rate if s_rate is None else s_rate))
