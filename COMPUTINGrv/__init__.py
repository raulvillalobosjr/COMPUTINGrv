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

def flip_bool(b):
    if int(b) == 1:
	    return 0
    else:
        return 1

def add_binary(a, b):
	return bin(a+b)[2:]

def flip(y):
	return int(not bool(y))

def is_empty(dictionary):
	return len(dictionary) == 0

def has_key(dictionary, key):
	return key in dictionary

def yeah_nope(b):
	return "yeah" if b else "nope"
