import numpy as np

def ORGAN01(w,t):
	try:
		y=np.sin(2*np.pi*w*t)+np.cos(np.pi*w*t)+np.sin(0.5*np.pi*w*t)+np.cos(0.25*np.pi*w*t)
		return y
	except Exception as e:
		raise e
