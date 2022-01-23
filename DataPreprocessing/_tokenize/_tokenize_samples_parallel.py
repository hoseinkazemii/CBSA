from ._tokenize_samples import _tokenize_samples

from multiprocessing import Queue, Process
import multiprocessing as mp

def _tokenize_samples_parallel(X, **params):

	n_cores = params.get("n_cores")
	replacements = params.get("replacements")

	results_queue = Queue()
	pool = []

	L = len(X)
	l_sections = int(L/n_cores) + 1

	print ("Assigning workers...")
	for j in range (n_cores):
		samples = X[j*l_sections: min((j+1)*l_sections, L)]

		worker = Process(target = _tokenize_samples,
						args = (samples,
								j,
								results_queue))

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


	holder = sorted(holder, key=lambda x: x[0])
	
	output = []
	for _, ls in holder:
		output += ls

	return output

