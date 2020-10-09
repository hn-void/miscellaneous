import time


def simple_collatz_rec_inner(n, count):
	count += 1
	if n == 1:
		return (1, count)
	else:
		if n % 2 == 0:
			return simple_collatz_rec_inner(n//2, count)
		else:
			return simple_collatz_rec_inner(n*3+1, count)


def simple_collatz_rec(n):
	return simple_collatz_rec_inner(n, 0)


def simple_collatz(n, done_set):
	if n <= 0:
		return -1
	count = 1
	while n != 1:
		if n in done_set:
			return n, 0
		count += 1
		if n % 2 == 0:
			n = n//2
		else:
			n = n*3+1
	return n, count


if __name__ == '__main__':
	done_set = set([])
	i = 0
	while True:
		i += 1
		start = time.time()
		print(i, simple_collatz(i, done_set), start-time.time())
		done_set.add(i)
