# AEDA: An Easier Data Augmentation Technique for Text classification
# Akbar Karimi, Leonardo Rossi, Andrea Prati

import random
import argparse
from os.path import dirname, basename, join

random.seed(0)

PUNCTUATIONS = ['.', ',', '!', '?', ';', ':']
# DATASETS = ['cr', 'sst2', 'subj', 'pc', 'trec']
# NUM_AUGS = [1, 2, 4, 8]
# PUNC_RATIO = 0.3

# Insert punction words into a given sentence with the given ratio "punc_ratio"
def insert_punctuation_marks(sentence, punc_ratio):
	words = sentence.split(' ')
	new_line = []
	q = random.randint(1, int(punc_ratio * len(words) + 1))
	qs = random.sample(range(0, len(words)), q)

	for j, word in enumerate(words):
		if j in qs:
			new_line.append(PUNCTUATIONS[random.randint(0, len(PUNCTUATIONS)-1)])
			new_line.append(word)
		else:
			new_line.append(word)
	new_line = ' '.join(new_line)
	return new_line

def main(args):
    output = args.output if args.output else join(dirname(args.input), 'aeda_' + basename(args.input))
    
    data_aug = []
    with open(args.input, 'r') as train_orig:
        for line in train_orig:
            line1 = line.split('\t')
            label = line1[0]
            sentence = line1[1]
            for i in range(args.num_aug):
                sentence_aug = insert_punctuation_marks(sentence, args.punc_ratio)
                line_aug = '\t'.join([label, sentence_aug])
                data_aug.append(line_aug)
            data_aug.append(line)

    with open(output, 'w') as aug_sentences:
        for aug in data_aug:
            aug_sentences.write(aug)
    
    print("generated augmented sentences with aeda for " + args.input + " to " + output + " with num_aug=" + str(args.num_aug))

# def main(dataset):
# 	for aug in NUM_AUGS:
# 		data_aug = []
# 		with open(dataset + '/train.txt', 'r') as train_orig:
# 			for line in train_orig:
# 				line1 = line.split('\t')
# 				label = line1[0]
# 				sentence = line1[1]
# 				for i in range(aug):
# 					sentence_aug = insert_punctuation_marks(sentence)
# 					line_aug = '\t'.join([label, sentence_aug])
# 					data_aug.append(line_aug)
# 				data_aug.append(line)

# 		with open(dataset + '/train_orig_plus_augs_' + str(aug) + '.txt', 'w') as train_orig_plus_augs:
# 			train_orig_plus_augs.writelines(data_aug)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='input file of unaugmented data')
    parser.add_argument('--output', required=False, help='output file of augmented data')
    parser.add_argument('--num_aug', type=int, default=9, help='number of augmented sentences per original sentence')
    parser.add_argument('--punc_ratio', type=float, default=0.3)
    args = parser.parse_args()
    
    main(args)
    
# 	for dataset in DATASETS:
# 		main(dataset)
