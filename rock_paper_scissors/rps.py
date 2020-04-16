#!/usr/bin/python

import sys

flatten = lambda l: [item for sublist in l for item in sublist]

def rock_paper_scissors(n):
	rps = ["rock", "paper", "scissors"]
	permutations = []

	if n <= 0:
		return [[]]
	
	elif n == 1:
		return [['rock'], ['paper'], ['scissors']]

	else:
		for i in range(0, n + 1):
			if (n >= len(rps)):
				for j in range(0, len(rps)):
					permutations.append((list(map(lambda xs: [rps[j]] + xs, rock_paper_scissors(n - 1)))))
			else:
				permutations.append(list(map(lambda xs: [rps[i]] + xs, rock_paper_scissors(n - 1))))

		cache = []
		for xs in permutations:
			if xs in cache:
				continue	
			else:
				 cache.append(xs)

		return flatten(cache)

		

if __name__ == "__main__":
	if len(sys.argv) > 1:
		num_plays = int(sys.argv[1])
		print(rock_paper_scissors(num_plays))
	else:
		print('Usage: rps.py [num_plays]')