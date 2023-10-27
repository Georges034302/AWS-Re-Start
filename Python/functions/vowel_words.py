# Req: Count the number of words with 2-vowels in a sentence
#   - Read sentences from STDIN

# count how many vowels
def vowel_count(word):    
    count = 0   
    for c in word:
        if c in "aeiou":
            count+=1
    return count

# find the matching words in a sentence
def matches(sentence):
    word_list = sentence.split(' ')
    count = 0
    for word in word_list:
        if(vowel_count(word) == 2):
            count +=1
    return count # number of vowel words

def run():
    sentence = input('sentence: ')
    
    while sentence != '*':
        print(f'Vowels count = {matches(sentence.lower())}')
        sentence = input('sentence: ')
run()