#!/usr/bin/env python

import string
import argparse

parser = argparse.ArgumentParser(description='Substitues every letter for a \
	single wildcard in a crossword word.')
parser.add_argument("mystery", help='Word you are trying to solve. Use * for \
	wildcard.')
args = parser.parse_args()

alpha = list(string.ascii_lowercase)

mystery_word = args.mystery

def alpha_sub(sub_this):
	for letter in alpha:
		print(sub_this.replace("*", letter))

alpha_sub(mystery_word)