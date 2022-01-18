
def segment_Y(Y, **params):
	Y_segments = params.get("Y_segments")
	Y_quantile = params.get("Y_quantile")

	print("segmenting Y")

	Y_quantile = Y.quantile(Y_quantile)
	holder = []

	for value in Y:

		if value <= Y_quantile:
			holder.append(0)
		else:
			holder.append(1)

	return holder