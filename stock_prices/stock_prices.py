#!/usr/bin/python

import argparse
from functools import reduce


def find_max_profit(prices):
	def reducer(acc, cur):
		starting_point = prices.index(cur) + 1 
		available_prices = prices[starting_point: len(prices)] 

		# this if guard prevents an index out of range error
		if starting_point != len(prices):
			acc.append(max(available_prices) - cur)
			
		return acc

	return max(reduce(reducer, prices, []))


if __name__ == '__main__':
	# This is just some code to accept inputs from the command line
	parser = argparse.ArgumentParser(description='Find max profit from prices.')
	parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
	args = parser.parse_args()

	print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))