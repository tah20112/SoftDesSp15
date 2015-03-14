""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
from pprint import pprint

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	book = open(file_name,'r')
	text = book.readlines()
	curr_line = 0
	while text[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	text = text[curr_line+1:]
	new_text = []

	for line in text:
		if 'THE END' in line or 'Project Gutenberg' in line:
			return new_text
		elif line == '\r\n':
			pass
		else:
			item = line.replace('-',' ')
			item_sans_punct = line.translate(string.maketrans("",""), string.punctuation)
			item_lower = item_sans_punct.lower()
			item_sans_rn = item_lower.strip('\r\n')
			list_of_words = item_sans_rn.split()
			for word in list_of_words:			new_text.append(word)


def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequently occurring
	"""
	word_counts = {}
	for word in word_list:
		if word not in word_counts:
			word_counts[word] = word_list.count(word)
	ordered_by_frequency = sorted(word_counts, key=word_counts.get, reverse=True)
	return ordered_by_frequency[0:n]

def print_top_n_words(file_name,n):
	word_list = get_word_list(file_name)
	pprint(get_top_n_words(word_list,n))

if __name__ == '__main__':
	print_top_n_words('Dracula.txt',100)