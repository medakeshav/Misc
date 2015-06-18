def hamming_distance(sentence, replace):
	dictionary = {}
	value
	words = sentence.split(' ')
	for word in words:
		if len(word) == len(replace):
			dictionary[word] = sum(w1 != r1 for w1, r1 in zip(word, replace))
	value = min(dictionary)
	words.index(value) = replace
	print ' '.join(words)

