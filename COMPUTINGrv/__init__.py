def And(a, b):
	return a and b	

lambda_func = lambda x : x

def check(lst, el):
	return el in lst

def ctoa(char):
	return ord(char)

def all_truthy(*args):
	lst = []
	for i in args:
		if bool(i) == True:
			lst.append(i)
	return len(args)==len(lst)
