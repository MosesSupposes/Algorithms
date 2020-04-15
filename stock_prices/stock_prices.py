#!/usr/bin/python

import argparse
from functools import reduce


def find_max_profit(prices):

	# Reducer
	def find_max_and_min(acc, cur):
		print("cur:", cur, "acc[min]:", acc["min"])
		if cur < acc["min"]:
			acc["min"] = cur

		if cur > acc["max"]: 
			acc["max"] = cur

		return acc

	min_and_max_prices = reduce(find_max_and_min, prices, {"max": 0, "min": 100000000000000000})
	print(min_and_max_prices)

	return min_and_max_prices["max"] - min_and_max_prices["min"]
	


if __name__ == '__main__':
	# This is just some code to accept inputs from the command line
	parser = argparse.ArgumentParser(description='Find max profit from prices.')
	parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
	args = parser.parse_args()

	print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))