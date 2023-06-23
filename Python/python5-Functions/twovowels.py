# Read a string from STDIN until * is entered
# Count and show the stretch of 2-vowels in the string (Matching words)
# A stretch of 2-vowels is: a segment of a word after a z or a word; containing exactly 2 vowels
# Example: 
# String: azoooza azooza zoo azoo
# Matching words: 3
# String: GONZALEZ passes the ball to VAZQUEZ
# Matching words: 3 (here the segment ALE, word passes, segment QUE )
# String: azozozee
# Matching words: 1  (here the segment zee is the match)
# Recommended approach, use the break-it-down build-it-up process

# Break it down - Build it up approach:
# top level objective: show the matching words (enter a sentence)
# word level: break down the sentence into words and count the matching words
# segment level: break down the words into segments (by z). check if a segment has 2 vowels
# vowel count level: count the vowels in a segment

# vowel count level
def vowel_count(segment):
    count = 0
    for c in segment:
        if c in "aiueo":
            count +=1
    return count

# segment level
def match(word):
    for segment in word.split("z"):
        if vowel_count(segment) == 2:
            return True
    else:
        return False
    
# word level
def word_count(sentence):
    count = 0
    for word in sentence.split(" "):
        if match(word):
            count += 1
    return count    

# top level: sentence
def show_matches():
    sentence = input("Sentence: ")    
    while sentence != "*":
        print(f"Matching words = {word_count(sentence.lower())}")
        sentence = input("Sentence: ")

show_matches()