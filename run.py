from DataLoader import *
from utils import *


def run(**params):
	settings = {
	"data_directory" : "./Data/analytics_challenge_dataset_ex210911.csv",
	"dropped_cols" : ["docid", "author*", "pubname", "region"],
	"inde_var" : "content",
	"de_var" : "share_count",
	"replacements":replacements








	}


	df = get_data(**settings)
	X, Y = split_data(df, **settings)
	X = tokenize(X,**settings)
	X = remove_spaces(X)
	

if __name__ == '__main__':
	run()
