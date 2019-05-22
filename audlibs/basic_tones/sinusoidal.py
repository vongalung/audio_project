import numpy as np

def SIN(w,t):
	try:
		y=np.sin(2*np.pi*w*t)
		return y
	except Exception as e:
		raise e

def COS(w,t):
	try:
		y=np.cos(2*np.pi*w*t)
		return y
	except Exception as e:
		raise e
