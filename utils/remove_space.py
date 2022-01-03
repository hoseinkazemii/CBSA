
def remove_space(_list,**params):
	removements=['', ' ',]

	for obj in removements:

		while obj in _list:
			_list.remove(obj)

	# return _list
	print(_list)