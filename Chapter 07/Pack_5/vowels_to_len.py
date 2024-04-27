# Define a string of vowels
vowels = 'aouei'
 
# Read input for n which will be the number of words
n = int(input())
 
# Initialize variables to keep track of the best word, maximum vowel count, and ratio
ratio = 1
# Initialize the best word as an empty string
best = ""
# Initialize the maximum vowel count as 0
max_vowels = 0
 
# Loop n times to process n words
for _ in range(n):
    word = input()
 
    vowels_in_word = 0
 
    # Loop through each character in the word
    for l in word:
        if l in vowels:
            vowels_in_word += 1
 
     # Compare the ratio of vowels to word length with the current best
    if vowels_in_word/len(word) < ratio:
        best = word
        max_vowels = vowels_in_word
        ratio = vowels_in_word/len(word)
    elif vowels_in_word/len(word) == ratio and vowels_in_word == max_vowels and len(best) < len(word):
        best = word
        max_vowels = vowels_in_word
        ratio = vowels_in_word/len(word)
    elif vowels_in_word/len(word) == ratio and vowels_in_word > max_vowels:
        best = word
        max_vowels = vowels_in_word
        ratio = vowels_in_word/len(word)
 
 
# Print the best word along with the maximum vowel count and length of the best word
print(f"{best} {max_vowels}/{len(best)}")