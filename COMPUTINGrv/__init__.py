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

def runningSum(nums):
    lst=[]
    y=1
    for i in nums:
        lst.append(sum(nums[:y]))
        y=y+1
    return lst

def element_from_set(s):
	return s.pop()

def cpp_txt(lst):
	return "".join(lst[:-1])

def NOT(num):
	return not num

def AND(num,num2):
	return num and num2

def OR(num,num2):
	return num or num2

def check_equals(lst1, lst2):
	return lst1 == lst2

def to_number_list(lst):
	lsti=[]
	for i in lst:
		lsti.append(float(i))
	return lsti

def last_ind(lst):
	if len(lst) == 0:
		return None
	else:
		return lst[-1]
