from pprint import pprint
import csv
import pandas as pd
import ast
from ast import literal_eval
import random


random.seed(0)

def insert_punctuation_marks(sentence):
	words = sentence.split(' ')
	new_line = []
	q = random.randint(1, int(len(words)/3)+1)
	qs = random.sample(range(0, len(words)), q)
	punctuations = ['.', ',', '!', '?', ';', ':']
	for j, word in enumerate(words):
		if j in qs:
			new_line.append(punctuations[random.randint(0, len(punctuations)-1)])
			new_line.append(word)
		else:
			new_line.append(word)
	new_line = ' '.join(new_line)
	return new_line


def main(datum):
	augs = [1, 2, 4, 8]
	for aug in augs:
		data_aug = []
		with open(datum+'/train_orig.txt', 'r') as train_orig:
			for line in train_orig:
				line1 = line.split('\t')
				label = line1[0]
				sentence = line1[1]
				for i in range(aug):
					sentence_aug = insert_punctuation_marks(sentence)
					line_aug = '\t'.join([label, sentence_aug])
					data_aug.append(line_aug)
				data_aug.append(line)

		with open(datum + '/train_aug_plus_orig_' + str(aug) + '.txt', 'w') as train_aug_plus_orig:
			train_aug_plus_orig.writelines(data_aug)


if __name__ == "__main__":
	data = ['cr', 'sst2', 'subj', 'pc', 'trec']
	for datum in data:
		main(datum)
