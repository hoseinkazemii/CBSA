import pandas as pd

def get_hsi(**params):
	hsi_dir = params.get("hsi_dir")
	hsi_selected_var = params.get("hsi_selected_var")

	df = pd.read_csv(hsi_dir)

	Y = df[hsi_selected_var]

	return(Y)