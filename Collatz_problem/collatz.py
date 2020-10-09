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


def simple_collatz(n):
	if n <= 0:
		return -1
	count = 1
	while n != 1:
		count += 1
		if n % 2 == 0:
			n = n//2
		else:
			n = n*3+1
	return n, count


if __name__ == '__main__':
	for i in range(1, 1000000):
		start = time.time()
		print(i, simple_collatz_rec(i), start-time.time())
