import numpy as np

def segment_Y(Y, **params):
	Y_segments = params.get("Y_segments")
	Y_quantile = params.get("Y_quantile")

	print("segmenting Y")

	Y = np.array(Y)
	Y = np.hstack(Y)

	Y_quantile = np.quantile(Y, Y_quantile, axis = 0)

	Y[Y > Y_quantile] = 1
	Y[Y <= Y_quantile] = 0

	return Y