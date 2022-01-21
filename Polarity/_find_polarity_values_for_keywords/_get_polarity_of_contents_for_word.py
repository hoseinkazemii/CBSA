import pandas as pd

from multiprocessing import Queue, Process
import multiprocessing as mp

from ._get_polarity_of_contents_for_word_process import _get_polarity_of_contents_for_word_process


def _get_polarity_of_contents_for_word(df, word, **params):

	n_cores = params.get("n_cores")

	results_queue = Queue()
	pool = []

	L = len(df)
	l_sections = int(L/n_cores) + 1

	print ("Assigning workers...")
	for j in range (n_cores):
		tmp_df = df.iloc[j*l_sections: min((j+1)*l_sections, L), :].copy()

		worker = Process(target = _get_polarity_of_contents_for_word_process,
						args = (tmp_df,
								word,
								results_queue,))

		pool.append(worker)

	for worker in pool:
		worker.start()
	print ("Workers started")

	holder = []

	while any(worker.is_alive() for worker in pool):
		while not results_queue.empty():
			sample = results_queue.get()

			if not sample is None:
				holder.append(sample)

	print ("Workers tying to join...")
	for worker in pool:
		worker.join()


	df = pd.concat(holder, axis = 0)
	df.sort_index(inplace = True)

	return df["sentiments"].values