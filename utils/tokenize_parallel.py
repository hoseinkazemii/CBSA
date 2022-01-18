from .tokenize import tokenize

from multiprocessing import Queue, Process
import multiprocessing as mp

def tokenize_parallel(X, **params):
	replacements = params.get("replacements")

	batch_size_for_tokenizer = X.shape[0]

	results_queue = Queue()
	n_cores = mp.cpu_count()-2

	pool = []

	for j in range (n_cores):
		worker = Process(target = tokenize, args = (X, replacements, ))

		pool.append(worker)

	for worker in pool:
		worker.start()

	holder = []

	while any(worker.is_alive() for worker in pool):
		while not results_queue.empty():
			sample = results_queue.get()

			if not sample is None:
				holder.append(sample)

	for worker in pool:
		worker.join()

	# return holder[:batch_size_of_generator]

	return holder

