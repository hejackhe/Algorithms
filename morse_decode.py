from collections import defaultdict


morse_dict = {'.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e', '..-.':'f', 
            '--.':'g', '....':'h', '..':'i', '.---':'j', '-.-':'k', '.-..':'l',
            '--':'m', '-.':'n', '---':'o', '.--.':'p', '--.-':'q', '.-.':'r',
            '...':'s', '-':'t', '..-':'u', '...-':'v', '.--':'w', '-..-':'x',
            '-.--':'y', '--..':'z', '.----':'1', '..---':'2', '...--':'3',
            '....-':'4', '.....':'5', '-....':'6', '--...':'7', '---..':'8',
            '----.':'9', '-----':'0'
            }

def morseDecode(morse_code):
    message = ''
    for code in morse_code:
        message += morse_dict.get(code)
    return message

def posb_word_update_from_char(i, word_list, m_dict):
    words = []
    for posb_word in word_list:
        if list(posb_word)[i] in m_dict[i]:
            words.append(posb_word)
        else:
            continue
    return(words)


def partialMorseDecode(partial_morse_code, dictionary):
    if len(partial_morse_code) > 0:
        possible_words = []
    # create dictionary of lists of possible characters from partial morse code
        m_dict = defaultdict(list)
        for i in range(len(partial_morse_code)):
            m_dict[i]
        for i in m_dict:
            for code in morse_dict:
                if len(partial_morse_code[i][1:]) == len(code[1:]) and list(partial_morse_code[i])[1:] == list(code)[1:]:
                    m_dict[i].append(morse_dict[code])
                else:
                    continue
    # shrink dictionary.txt space by len(word) = len(morse)
        for word in dictionary:
            if len(word) == len(m_dict):
                possible_words.append(word.lower())
            else:
                continue
        # recursively refactor the possible_words list for each character in morse code
        for i in range(len(m_dict)):
            possible_words = posb_word_update_from_char(i, possible_words, m_dict)
        return(possible_words)
    else:
        return('Error: No morse code to decode')

if __name__ == '__main__':
    with open('dictionary.txt', 'r') as f:
        dictionary = f.read().splitlines()
    pass


#morse_code = ['--.','.-.','.','.','-','..','-.','--.','...','.----','..---','---..'] # greetings128
partial_morse_code = ['x-.','x-.','x','x','x','x.','x.','x-.'] #greeting
#partial_morse_code = ['x.-','x.','x-','x..','x..-','x','x.','x','x.-','x-.','x','x..']    # unadventured
#partial_morse_code = ['x.-','x-.','x..'] # urs
#partial_morse_code = ['x...','x.']
#print(morseDecode(morse_code))
print(partialMorseDecode(partial_morse_code, dictionary))
#b = "a" > "c"
#print(list('hiiiiiiiiiiiiiiiiiiii'))
#print(b)
#print(list(dictionary[1]))
#print(list('hi')[0])