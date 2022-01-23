import time
import json

from multiprocessing import Queue, Process
import multiprocessing as mp

def remove_stop_words(X, **params):
	"""
	X: list of list
	"""
	print("removing stop words...")

	stop_words_dir = params.get("stop_words_dir")
	with open("./DataPreprocessing/_text_cleaners/stopwords-zh.json",
				'r', encoding = 'utf-8-sig') as f:
		stop_words = json.load(f)	

	n_cores = params.get("n_cores")

	results_queue = Queue()
	pool = []

	L = len(X)
	l_sections = int(L/n_cores) + 1

	print ("--- Assigning workers...")
	for j in range (n_cores):
		samples = X[j*l_sections: min((j+1)*l_sections, L)]

		worker = Process(target = _remove_stop_words_for_process,
						args = (samples,
								stop_words,
								j,
								results_queue))
		pool.append(worker)

	for worker in pool:
		worker.start()
	print ("--- Workers started")

	holder = []

	while any(worker.is_alive() for worker in pool):
		while not results_queue.empty():
			sample = results_queue.get()

			if not sample is None:
				holder.append(sample)

	print ("--- Workers tying to join...")
	for worker in pool:
		worker.join()


	holder = sorted(holder, key=lambda x: x[0])
	
	X = []
	for _, X_ls in holder:
		X += X_ls

	return X



def _remove_stop_words_for_process(X,
								stop_words,
								batch_number,
								results_queue):

	for sw in stop_words:
		for sentence in X:
			try:
				while True:
					sentence.remove(sw)
			except ValueError:
				pass

	results_queue.put((batch_number, X))

