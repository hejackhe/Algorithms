import itertools
from collections import defaultdict

morse_dict = {'.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e', '..-.':'f', 
            '--.':'g', '....':'h', '..':'i', '.---':'j', '-.-':'k', '.-..':'l',
            '--':'m', '-.':'n', '---':'o', '.--.':'p', '--.-':'q', '.-.':'r',
            '...':'s', '-':'t', '..-':'u', '...-':'v', '.--':'w', '-..-':'x',
            '-.--':'y', '--..':'z', '.----':'1', '..---':'2', '...--':'3',
            '....-':'4', '.....':'5', '-....':'6', '--...':'7', '---..':'8',
            '----.':'9', '-----':'0'
            }

def morseDecode(inputStringList):
	"""
	This method takes a list of strings as input where each string is equivalent to one letter
	The entire list of strings represents a word.
	This method converts the strings from morse code and returns the decoded word as a string.
	"""
	message = ''
	for code in inputStringList:
		message += morse_dict.get(code)
	return(message)

# additional method to be recursively called within morsePartialDecode
def posb_word_update_from_char(i, word_list, m_dict):
# given a search space as a parameter, it checks if the character at position i is 
# a valid character from the collection of decoded characters at position i in partial morse code
# it then returns an updated search space "words"
    words = []
    for posb_word in word_list:
        if list(posb_word)[i] in m_dict[i]:
            words.append(posb_word)
        else:
            continue
    return(words)

def morsePartialDecode(inputStringList):
	"""
	This method takes a list of strings as input where each string is equivalent to one letter
    and the entire list of strings represents a word.
	However, the first character of every morse code string is unknown (represented by 'x')
	For example, TEST = ['-','.','...','-']
	However, with the first characters missing, TEST = ['x','x','x..','x']
	With x unknown, the word could be TEST, EESE, ETSE, ETST, EEDT or other permutations.
	This function finds and returns a list of all possible valid words defined in dictionary.txt
	"""
	# first check if the input is a valid input
	if len(inputStringList) > 0:
		possible_words = []
	# read the valid words from dictionary.txt and save as "dictionary"
		dictionaryFileLoc = './dictionary.txt'
		with open(dictionaryFileLoc, 'r') as f:
			dictionary = f.read().splitlines()
		pass
 	# create dictionary where keys are the position of each character in partial morse code, 
	# and its values are lists of possible characters according to morse_dict based on the characters in morse code following "x"
		m_dict = defaultdict(list)
		for i in range(len(inputStringList)):
		    m_dict[i]
		for i in m_dict:
		    for code in morse_dict:
		        if len(inputStringList[i][1:]) == len(code[1:]) and list(inputStringList[i])[1:] == list(code)[1:]:
		            m_dict[i].append(morse_dict[code])
		        else:
		            continue
	# initialise starting search space, where possible_words is a list of equal length valid words from "dictionary"
		for word in dictionary:
		    if len(word) == len(m_dict):
		        possible_words.append(word.lower())
		    else:
		        continue
	# recursively reduce the size of the problem for each character in morse code, updating possible_words at each step until arriving at solution
		for i in range(len(m_dict)):
		    possible_words = posb_word_update_from_char(i, possible_words, m_dict)
		return(possible_words)
	else:
		print('Error: No morse code to decode')
		return([])
	pass


def morseCodeTest():
	hello = ['....','.','.-..','.-..','---']
	print(morseDecode(hello))

def partialMorseCodeTest():
	# This is a partial representation of the word TEST, amongst other possible combinations
	test = ['x','x','x..','x']
	t1 = ["x...", "x-", "x-.", "x-.", "x.--"]
	t2 = ["x...", "x-", "x-."]
	t3 = ["x.-.", "x-", "x-."]
	t4 = ["x...", "x-", "x-..", "x-.."]
	print(morsePartialDecode(test))
	print(morsePartialDecode(t1))
	print(morsePartialDecode(t2))
	print(morsePartialDecode(t3))
	print(morsePartialDecode(t4))

	# This is a partial representation of the word DANCE, amongst other possible combinations
	dance = ['x..','x-','x.','x.-.','x']
	print(morsePartialDecode(dance))


def main():
	morseCodeTest()
	partialMorseCodeTest()
	

if(__name__ == "__main__"):
	main()
