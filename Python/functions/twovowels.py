# Req: Read a string from STDIN until *
# count and show the stretch of 2 vowels
# 
# Stretch of 2-vowels is a segment of a word after a a z 
# or a word; containing exactly 2 vowels
# 
# Example: 
# String: azoooza azooza zoo azoo
# Matching words: 3
# String: GONZALEZ passes the ball to VAZQUEZ
# Matching words: 3

# count how many vowels in a segment
def vowel_count(segment):    
    count = 0   
    for c in segment:
        if c in "aeiou":
            count+=1
    return count

# break down a word into segments after a z
def match(word):
    for segment in word.split('z'):
        if vowel_count(segment) == 2:
            return True
        
# break down a string into words after a white-space
def word_count(string):
    count = 0
    for word in string.split(' '):
        if match(word):
            count +=1
    return count 

def show_matches():
    s = input('Sentence: ')
    while s != '*':
        print(f'Matching words = {word_count(s.lower())}')
        s = input('Sentence: ')
        
show_matches()

